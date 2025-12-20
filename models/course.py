from odoo import fields,models,api
class Course(models.Model):
    _name = 'institution.course'
    _description = 'Course'
    name = fields.Char(string='Course Name',required=True)
    code = fields.Char(string='Course Code',required=True)
    description = fields.Text(string='Course Description')
    duration = fields.Integer(string='Duration(months)')

    category_ids=fields.Many2one('institution.category',string='Category',required=True)
    teacher_id = fields.Many2one('institution.teacher',string='Teacher')


    batch_id=fields.One2many('institution.batch','course_ids',string='Batch')
    batch_count=fields.Integer(compute='_compute_batch_count',store=True)
    student_count=fields.Integer(compute='_compute_student_count',string='Student Count')

    @api.depends('batch_id')
    def _compute_batch_count(self):
        for count in self:
            count.batch_count = len(count.batch_id)

    def _compute_student_count(self):
        for count in self:
            count.student_count=sum(len(batch.student_id) for batch in count.batch_id)

























