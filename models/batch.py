from odoo import fields,models
class Batch(models.Model):
    _name = 'institution.batch'
    _description = 'Institutional batch'
    name = fields.Char(string='Batch Name',required=True)
    course_id = fields.Many2one('institution.course', string='Course')
    start_date=fields.Datetime(string='Start Date',required=True)
    end_date=fields.Datetime(string='End Date',required=True)
    status=fields.Selection([
                              ('running','Running'),
                              ('completed','Completed')], string='Status',default='running',store=True)

    student_ids = fields.One2many('institution.student','batch_id',string='Student')

