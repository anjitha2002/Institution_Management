from datetime import date
from odoo import fields,models,api

class Batch(models.Model):
    _name = 'institution.batch'
    _description = 'Institutional batch'
    name = fields.Char(string='Batch Name',required=True)
    course_ids = fields.Many2one('institution.course', string='Course',required=True)
    start_date=fields.Date(required=True)
    end_date=fields.Date()

    student_id = fields.One2many('institution.student','batch_id',string='Student')
    student_count = fields.Integer(compute='_compute_student_count',store=True)

    status=fields.Selection([
                              ('running','Running'),
                              ('completed','Completed'),
                              ('dropped','Dropped')], compute='_compute_status',store=True)

    @api.depends('student_id')
    def _compute_student_count(self):
        for count in self:
            count.student_count=len(count.student_id)

    @api.depends('end_date')
    def _compute_status(self):
        today=date.today()
        for batch in self:
            if batch.end_date and batch.end_date < today:
               batch.status='completed'
            elif batch.end_date and batch.end_date > today:
                batch.status='running'
            else:
                batch.status='dropped'
