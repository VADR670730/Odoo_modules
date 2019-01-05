# -*- coding: utf-8 -*-

from odoo import models, fields, api

class relation_externe(models.Model):
    _name = "relation.externe"  # Table in DB => car_request
    _inherit = ['mail.thread']
    _description = "Relation externe internation"

    name = fields.Char(string="Demande", required=True, )
    motive = fields.Char(string="Motivation", required=True, )
    date_from = fields.Datetime(string="Date début", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="Date retour", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    state = fields.Selection(string="Statut", selection=[('draft', 'Draft'), ('confirm', 'Confirmée'),
                                                         ('validate', 'Valide'), ('refuse', 'Refusée'),
                                                         ('approved', 'Approvée'), ], default="draft",
                             track_visibility='onchange', )

    @api.multi
    def confirm_request(self):
        self.state = 'confirm'

    @api.multi
    def validate_request(self):
        self.state = 'validate'

    @api.multi
    def refuse_request(self):
        self.state = 'refuse'

    @api.multi
    def approve_request(self):
        self.state = 'approved'