from email.policy import default

from odoo import api, fields, models
class Attendance(models.Model):
    _name = 'institution.attendance'
    _description = 'Attendance'
    date=fields.Date(string='Date of Attendance',default=fields.Date.today)
    student_id = fields.Many2one('institution.student', required=True)
    # batch_id=fields.Many2one(related='student_id.batch_id',store=True)

    status=fields.Selection([('present','Present'),('absent','Absent')],required=True)


