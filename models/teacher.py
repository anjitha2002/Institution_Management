from odoo import fields,models,api
class Teacher(models.Model):
    _name = "institution.teacher"
    _description = 'Teacher'

    user_id=fields.Many2one('res.users',string='User',ondelete='cascade')
    name = fields.Char(string='Teacher Name',required=True)

    phone = fields.Char(string='Phone Number',required=True)
    email = fields.Char(string='Email Address',required=True)
    experience = fields.Text(string='Experience',required=True)




    course_ids = fields.One2many('institution.course','teacher_id',string='Course')

    course_count=fields.Integer(compute='_compute_course_count',store=True)

    @api.depends('course_ids')
    def _compute_course_count(self):
        for course in self:
            course.course_count = len(course.course_ids)