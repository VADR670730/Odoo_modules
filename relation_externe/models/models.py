# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import dateutil
class demande_charge(models.Model):
    _name = "demande.charge"  #Nom de latable dan la base de donnée  => demande_charge
    _inherit = ['mail.thread']    #Hériter le module mail pour l'envoie des email lors du changement d'état de la demande (refus...)
    _description = "Faire une demande de prise en charge dans le cadre d'un stage, séminaire, ou conférence pou les post-graduation"

    name = fields.Char(string="Titre de la demande", required=True, )   #Titre de la demane
    motive = fields.Char(string="Motivation", required=True, )   #La raison de vouloire participer
    date_from = fields.Datetime(string="Date début", default=fields.Datetime.now(), )  #date de départ
    date_to = fields.Datetime(string="Date retour", required=False, )  #date de retour
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )  #l'id de l'employé
    state = fields.Selection(string="Statut", selection=[('draft', 'Draft'),('incomplet','Incomplet'), ('confirm', 'Confirmée'),
                                                         ('validate', 'Valide'), ('refuse', 'Refusée'),
                                                         ('approved', 'Approvée'), ], default="draft",
                             track_visibility='onchange', ) #l'état de la demande
    user_id = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)
    file = fields.Binary("Attachment")

    file_name = fields.Char("Invitation")

    @api.multi
    def confirm_request(self):   #action de confirmation
        self.state = 'confirm'

    @api.multi
    def validate_request(self):   #action de validation demande
        self.state = 'validate'

    @api.multi
    def refuse_request(self):   #action  de refus
        self.state = 'refuse'

    @api.multi
    def approve_request(self):   #action d'approuver
        self.state = 'approved'

    @api.multi
    def incomplet_request(self):  # action d'approuver
        self.state = 'incomplet'

    @api.multi
    def action_bon_commande(self, context=None):
        action = self.env.ref('relation_externe.action_bon_commandelS').read()[0]
        return action


class bon_commande(models.Model):
    _name = "bon.commande"  #Nom de latable dan la base de donnée  => bon_commande
    _inherit = ['mail.thread']
    _description = "Creer des bons de commande pour les doctorants ayant été approuvé"

    name = fields.Char(string="Numéro du bon", required=True, )
    date_from = fields.Datetime(string="Date début", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="Date retour", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    value=fields.Float(string="Montant", default=100,required=True)  #le montant de la comande

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
        return self.env.ref('relation_externe.bon_commande_report').report_action(self, data=data)


class ReportBonCommande(models.AbstractModel):
    """Abstract Model for report template.
    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.relation_externe.bon_commande_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_from = dateutil.parser.parse(data['form']['date_from']).date()
        date_to = dateutil.parser.parse(data['form']['date_to']).date()
        name=data['form']['name']
        employee_id=data['form']['employee_id']
        value=data['form']['value']



        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'name': name,
            'employee_id': employee_id,
            'value': value,
            'date_from': date_from,
            'date_to': date_to,

        }
