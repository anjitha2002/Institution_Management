from odoo import models,fields
class Student(models.Model):
    _name = 'institution.student'
    _description = 'Student'
    name = fields.Char(string='Name', required=True)
    student_no=fields.Char(string='Student Number', readonly=True,default=lambda self:self.env['ir.sequence'].next_by_code('institution.student'))
    date_of_birth = fields.Datetime(string='Date of Birth', required=True)
    age = fields.Integer(string='Age', required=True)
    guardian_name = fields.Char(string='Guardian Name', required=True)
    guardian_phone=fields.Char(string='Guardian Phone', required=True)
    course_id = fields.Many2one('institution.course',string='Course')
    batch_id = fields.Many2one('institution.batch',string='Batch')
    # fees_paid = fields.Boolean(string='Fees Paid')
    fees_status=fields.Selection([
        ('paid','Paid'),
        ('pending','Pending')
    ],string='Fees Status',default='pending',store=True)









