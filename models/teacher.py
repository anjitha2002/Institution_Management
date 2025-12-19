from odoo import fields,models
class Teacher(models.Model):
    _name = "institution.teacher"
    _description = 'Teacher'
    name = fields.Char(string='Teacher Name',required=True)

    phone = fields.Char(string='Phone Number',required=True)
    email = fields.Char(string='Email Address',required=True)
    experience = fields.Text(string='Experience',required=True)



    # department_id = fields.Many2one('institution.department',string='Department')
    course_ids = fields.One2many('institution.course','teacher_id',string='Course')