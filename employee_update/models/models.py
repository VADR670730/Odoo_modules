# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee_update(models.Model):
    _inherit = "hr.employee"
    res_group_id = fields.Many2many('res.groups', 'rel_faculty_group', string="Assign Group", required=True)

    @api.model
    def create(self, values):
        is_active = values.get('is_active', False)
        if is_active:
            values['is_active'] = True
        else:
            values['is_active'] = True
        group_id = values.get('res_group_id', False)

        login = values.get('login', False)
        if login:
            values['login'] = login.lower()
            values['email'] = values['login']
            user = self.env['res.users'].search([('login', '=', values['login'])])
            if user:
                raise ValidationError('User already exist.')
            else:
                user = self.env['res.users'].create(
                    {'login': values['login'], 'name': values['name'], 'department_id': values['department_id']})
        employeeUser = super(employee_table, self).create(values)
        user.write({'faculty_id': employeeUser.id})

        if user:
            partner = self.env['res.partner'].search([('id', '=', user.partner_id.id)])
            if partner:
                partner.write({'email': values['login']})

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

    @api.multi
    def write(self, values):

        def sync_lists(db_list, ui_list):

            same_ui_list = [l for l in db_list if l in ui_list]
            remove_ui_list = [l for l in db_list if l not in ui_list]
            new_ui_list = [l for l in ui_list if l not in db_list]
            if new_ui_list != []:
                result = set(new_ui_list)
            else:
                result = set(same_ui_list) - set(remove_ui_list)
            return result, remove_ui_list

        faculty_user = self.env['res.users'].search([('faculty_id', '=', self.id)])
        partner = self.env['res.partner'].search([('id', '=', faculty_user.partner_id.id)])
        group_id = values.get('res_group_id', False)
        is_active = values.get('is_active')
        login = values.get('login', False)
        if login:
            values['login'] = login.lower()
            values['email'] = values['login']
            partner.write({'email': values['login']})

        # Below code is for add/delete groups in employee form -->Start
        if (group_id) and group_id[0][2]:
            ui_list = group_id[0][2]

            db_list = []
            self.env.cr.execute("""select gid from res_groups_users_rel where uid = """ + str(faculty_user.id))
            db_list = group_list = self.env.cr.fetchall()
            if group_list:
                group_list = [x[0] for x in group_list]
            temp_group = self.env['res.groups'].search([('id', 'in', group_list), ('is_lms_group', '=', True)])
            if temp_group:
                db_list = temp_group.ids
                group_list = temp_group.ids

            result, remove_ui_list = sync_lists(group_list, ui_list)
            for each in result:
                if each in db_list:
                    pass
                else:
                    self.env.cr.execute("""insert into res_groups_users_rel(gid,uid) values(""" + str(each) + """,""" + str(
                        faculty_user.id) + """)""")
                    self.env.cr.commit()
            for each in remove_ui_list:
                self.env.cr.execute(
                    """delete from res_groups_users_rel where uid=""" + str(faculty_user.id) + """ and gid = """ + str(
                        each))
                self.env.cr.commit()
        # Above code is for add/delete groups in employee form -->End

        if is_active:
            self.env.cr.execute("""select id from res_users where faculty_id = """ + str(self.id))
            uid = self.env.cr.fetchone()
            if uid:
                self.env.cr.execute("""update res_users set active=True where id = """ + str(uid[0]))
                self.env.cr.commit()
            if self.res_group_id:
                for g in self.res_group_id.ids:
                    self.env.cr.execute("""insert into res_groups_users_rel(gid,uid) values(""" + str(g) + """,""" + str(
                        faculty_user.id) + """)""")
                    self.env.cr.commit()
        elif is_active == False:
            faculty_user.write({'active': False})
        result = super(faculty, self).write(values)
        return result
