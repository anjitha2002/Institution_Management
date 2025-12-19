from odoo import fields,models
class Course(models.Model):
    _name = 'institution.course'
    _description = 'Course'
    name = fields.Char(string='Course Name',required=True)
    code = fields.Char(string='Course Code',required=True)
    description = fields.Text(string='Course Description',required=True)
    duration = fields.Integer(string='Duration',required=True)
    teacher_id = fields.Many2one('institution.teacher',string='Teacher')

    # credits=fields.Integer(string=' Credits')
    #
    # department_id=fields.Many2one('institution.department',string='Department')
    #

    student_ids=fields.One2many('institution.student','course_id',string='Student')
    category_ids=fields.Many2many('institution.category',string='Category')


























