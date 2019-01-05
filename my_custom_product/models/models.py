# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_custom_product(models.Model):
    _inherit="product.product"
    price_3=fields.Float(string="Price 3")
    other=fields.Char(string = "Other")