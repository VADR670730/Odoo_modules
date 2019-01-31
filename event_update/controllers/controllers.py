# -*- coding: utf-8 -*-
from odoo import http

# class EventUpdate(http.Controller):
#     @http.route('/event_update/event_update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_update/event_update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_update.listing', {
#             'root': '/event_update/event_update',
#             'objects': http.request.env['event_update.event_update'].search([]),
#         })

#     @http.route('/event_update/event_update/objects/<model("event_update.event_update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_update.object', {
#             'object': obj
#         })