# -*- coding: utf-8 -*-
from odoo import http

# class RelationExterne(http.Controller):
#     @http.route('/relation_externe/relation_externe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/relation_externe/relation_externe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('relation_externe.listing', {
#             'root': '/relation_externe/relation_externe',
#             'objects': http.request.env['relation_externe.relation_externe'].search([]),
#         })

#     @http.route('/relation_externe/relation_externe/objects/<model("relation_externe.relation_externe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('relation_externe.object', {
#             'object': obj
#         })