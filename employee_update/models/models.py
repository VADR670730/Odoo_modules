# -*- coding: utf-8 -*-
from odoo import exceptions
from odoo import models, fields, api

class employee_update(models.Model):
    _inherit = "hr.employee"
    res_group_id = fields.Many2many('res.groups', 'rel_employee_group', string="Groupe", required=True)

    @api.model
    def create(self, values):
        is_active = values.get('active', False)
        if is_active:
            values['active'] = True
        else:
            values['active'] = True
        group_id = values.get('res_group_id', False)

        login=values.get('work_email', False)
        name=values.get('name', False)
        values['login'] = login.lower()
        user = self.env['res.users'].search([('login', '=', values['login'])])
        values['work_email']=login.lower()
        if user:
            raise exceptions.ValidationError('User already exist.')
        else:
            user = self.env['res.users'].create(
                    {'login': values['login'], 'email':values['login'],'name': values['name'], 'department_id': values['department_id']})
            values['user_id']=user.id
            values['email'] = login.lower()
        employeeUser = super(employee_update, self).create(values)
        user.write({'employee_id': employeeUser.id})


        # group logic
        if (group_id) and group_id[0][2]:
            g_list = []
            for g in group_id:
                g_list = g[2]
            for g in g_list:
                self.env.cr.execute(
                    """insert into res_groups_users_rel(gid,uid) values(""" + str(g) + """,""" + str(user.id) + """)""")
                self.env.cr.commit()
        return employeeUser



