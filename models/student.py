from datetime import date
from typing import Self

from odoo import models,fields,api
from odoo.orm.decorators import readonly
from odoo.orm.types import ValuesType


class Student(models.Model):
    _name = 'institution.student'
    _description = 'Student'
    name = fields.Char(string='Name', required=True)
    student_no=fields.Char(default=lambda self: ('New'),readonly=True,index=True,copy=False,required=True)

    date_of_birth = fields.Datetime(string='Date of Birth', required=True)
    age = fields.Integer(compute='_compute_age',string='Age',store=True)

    guardian_name = fields.Char(string='Guardian Name', required=True)
    guardian_phone=fields.Char(string='Guardian Phone', required=True)

    course_ids = fields.Many2one(related='batch_id.course_ids',string='Course',store=True)
    batch_id = fields.Many2one('institution.batch',string='Batch',required=True)

    fee_payment_ids=fields.One2many('institution.fee_payment','student_id')
    total_fees_paid=fields.Float(compute='_compute_fees',store=True)
    fees_status=fields.Selection([
        ('paid','Paid'),
        ('pending','Pending')
    ],compute='_compute_fees',store=True)

    attendance_ids=fields.One2many('institution.attendance','student_id')


    attendance_percentage=fields.Float(compute='_compute_attendance',store=True)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for total in self:
            if total.date_of_birth:
                total.age = date.today().year - total.date_of_birth.year
            else:
                total.age = 0

    def _compute_fees(self):
        for f in self:
            paid=sum(f.fee_payment_ids.filtered(lambda p: p.status == 'paid').mapped('amount'))
            f.total_fees_paid=paid
            f.fees_status='paid' if paid > 0 else 'pending'

    def _compute_attendance(self):
        for a in self:
            total=len(a.attendance_ids)
            present=len(a.attendance_ids.filtered(lambda p: p.status == 'present'))
            a.attendance_percentage=(present/total*100) if total else 0

    @api.model
    def create(self, vals):
        if vals.get('student_no' ,('New'))==('New'):
            vals['student_no']=self.env['ir.sequence'].next_by_code('institution.student') or ('New')
            return super(Student, self).create(vals)









