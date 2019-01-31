# -*- coding: utf-8 -*-
from odoo import http

# class AttendanceRecapReportWizard(http.Controller):
#     @http.route('/attendance_recap_report_wizard/attendance_recap_report_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/attendance_recap_report_wizard/attendance_recap_report_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('attendance_recap_report_wizard.listing', {
#             'root': '/attendance_recap_report_wizard/attendance_recap_report_wizard',
#             'objects': http.request.env['attendance_recap_report_wizard.attendance_recap_report_wizard'].search([]),
#         })

#     @http.route('/attendance_recap_report_wizard/attendance_recap_report_wizard/objects/<model("attendance_recap_report_wizard.attendance_recap_report_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attendance_recap_report_wizard.object', {
#             'object': obj
#         })