# -*- coding: utf-8 -*-
from odoo import http

# class DocRequest(http.Controller):
#     @http.route('/doc_request/doc_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doc_request/doc_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doc_request.listing', {
#             'root': '/doc_request/doc_request',
#             'objects': http.request.env['doc_request.doc_request'].search([]),
#         })

#     @http.route('/doc_request/doc_request/objects/<model("doc_request.doc_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doc_request.object', {
#             'object': obj
#         })