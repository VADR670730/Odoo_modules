# -*- coding: utf-8 -*-
from odoo import http

# class MyCustomProduct(http.Controller):
#     @http.route('/my_custom_product/my_custom_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_custom_product/my_custom_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_custom_product.listing', {
#             'root': '/my_custom_product/my_custom_product',
#             'objects': http.request.env['my_custom_product.my_custom_product'].search([]),
#         })

#     @http.route('/my_custom_product/my_custom_product/objects/<model("my_custom_product.my_custom_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_custom_product.object', {
#             'object': obj
#         })