from email.policy import default

from odoo import api, fields, models
class Attendance(models.Model):
    _name = 'institution.attendance'
    _description = 'Attendance'
    date=fields.Date(string='Date of Attendance',default=fields.Date.today)
    batch_id=fields.Many2one('institution.batch',string='Batch')
    student_id=fields.Many2one('institution.student',string='Student')
status=fields.Selection([('present','Present'),('absent','Absent')],default="present" )


