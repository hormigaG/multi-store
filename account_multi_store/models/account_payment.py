##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = "account.payment"

    store_id = fields.Many2one(
        related="journal_id.store_id",
        store=True,
    )


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    store_id = fields.Many2one(
        related="journal_id.store_id",
        store=True,
    )
