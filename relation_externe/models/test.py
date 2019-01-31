from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class bon_commande_wizzard(models.TransientModel):
    _name = 'bon.commande.wizard'

    name = fields.Char(string="Numéro du bon", required=True, )
    date_from = fields.Datetime(string="Date début", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="Date retour", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    value = fields.Float(string="Montant", default=100, required=True)  # le montant de la comande

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'name': self.name,
                'employee_id': self.employee_id,
                'value':self.value,
                'date_from': self.date_from,
                'date_to': self.date_to,
            },
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('relation_externe.recap_report').report_action(self, data=data)


class bon_commande_recap(models.AbstractModel):
    """Abstract Model for report template.
    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.relation_externe.bon_commande_recap_report_view'

    @api.model
    def get_report_values(self, docids, data=None):
        date_start = datetime.strptime(data['form']['date_start'], DATE_FORMAT)
        date_end = datetime.strptime(data['form']['date_end'], DATE_FORMAT) + timedelta(days=1)
        date_diff = (date_end - date_start).days

        docs = []
        employees = self.env['hr.employee'].search([], order='name asc')
        for employee in employees:
            presence_count = self.env['hr.attendance'].search_count([
                ('employee_id', '=', employee.id),
                ('check_in', '>=', date_start.strftime(DATETIME_FORMAT)),
                ('check_out', '<', date_end.strftime(DATETIME_FORMAT)),
            ])

            absence_count = date_diff - presence_count

            docs.append({
                'employee': employee.name,
                'presence': presence_count,
                'absence': absence_count,
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start.strftime(DATE_FORMAT),
            'date_end': (date_end - timedelta(days=1)).strftime(DATE_FORMAT),
            'docs': docs,
        }