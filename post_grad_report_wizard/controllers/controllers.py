# -*- coding: utf-8 -*-
from odoo import http

# class PostGradReportWizard(http.Controller):
#     @http.route('/post_grad_report_wizard/post_grad_report_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/post_grad_report_wizard/post_grad_report_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('post_grad_report_wizard.listing', {
#             'root': '/post_grad_report_wizard/post_grad_report_wizard',
#             'objects': http.request.env['post_grad_report_wizard.post_grad_report_wizard'].search([]),
#         })

#     @http.route('/post_grad_report_wizard/post_grad_report_wizard/objects/<model("post_grad_report_wizard.post_grad_report_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('post_grad_report_wizard.object', {
#             'object': obj
#         })