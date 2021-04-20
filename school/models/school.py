# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SchoolProfile(models.Model):
    _name = 'school.profile'

    name = fields.Char(string="School Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    category_id = fields.Many2one(comodel_name='school.category', string='Category') 


