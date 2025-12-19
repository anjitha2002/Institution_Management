from odoo import fields,models
class Fee_payment(models.Model):
    _name = 'institution.fee_payment'
    _description = 'Fee Payment'
    student_id = fields.Many2one('institution.student',string='Student',required=True)
    amount = fields.Float(string='Amount')
    payment_date = fields.Datetime(string='Payment Date')
    status = fields.Selection([('paid','Paid'),('pending','Pending')],default='pending')