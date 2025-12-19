from odoo import fields,models
class Category(models.Model):
    _name='institution.category'
    _description='Category'
    name=fields.Char(string='Name',required=True)
    course_ids=fields.One2many('institution.course','category_ids',string='Courses')
