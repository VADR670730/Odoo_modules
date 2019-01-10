# -*- coding: utf-8 -*-

from odoo import models, fields, api

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


class bon_commande(models.Model):
    _name = "bon.commande"  #Nom de latable dan la base de donnée  => bon_commande
    _inherit = ['mail.thread']
    _description = "Creer des bons de commande pour les doctorants ayant été approuvé"

    name = fields.Char(string="Numéro du bon", required=True, )
    date_from = fields.Datetime(string="Date début", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="Date retour", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    value=fields.Float(string="Montant", default=100,required=True)  #le montant de la comande