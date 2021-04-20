# # -*- coding: utf-8 -*-

# from odoo import models, fields, api, _

# class School(models.Model):
#     _name = 'school.category'
#     _description = 'Data School Category'

#     name = fields.Char(
#         string='School Category Name',
#         required=True,
#         help="Fill school category name..."
#     )

#     description = fields.Text(
#         string='Description',
#     )

#     active = fields.Boolean(
#         string='Active', 
#         default=True
#     )

#     school_ids = fields.One2many(
#         comodel_name='school.profile',
#         inverse_name='category_id',
#         string='School'
#     )
    

#     # -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SchoolCategory(models.Model):
    _name = 'school.category'

    name = fields.Char(string="Category Name")
    description = fields.Char(string="Description")
    school_ids = fields.One2many(comodel_name='school.profile', inverse_name='category_id', string='School')
    