from odoo import fields,models
class Fee_payment(models.Model):
    _name = 'institution.fee_payment'
    _description = 'Fee Payment'
    student_id = fields.Many2one('institution.student',required=True,ondelete='cascade')
    amount=fields.Float(string='Amount',required=True)
    payment_date = fields.Datetime(string='Payment Date',default=fields.Datetime.now)

    status = fields.Selection([('paid','Paid'),('pending','Pending')],default='pending')