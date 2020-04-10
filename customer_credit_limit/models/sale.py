# See LICENSE file for full copyright and licensing details.


from odoo import api, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def check_limit(self):
        self.ensure_one()
        partner = self.partner_id
        moveline_obj = self.env['account.move.line']
        movelines = moveline_obj.search(
                [('partner_id', '=', partner.id),
                 ('account_id.user_type_id.name', 'in',['Receivable', 'Payable']),
                 ('full_reconcile_id', '=', False)]
            )

        debit, credit = 0.0, 0.0
        for line in movelines:
            credit += line.credit
            debit += line.debit

        existing_orders  = self.search([('partner_id', '=', partner.id),('invoice_status','=','to invoice'),('id','!=',self.id)])
        to_be_invoiced  = 0.0
        for order in existing_orders :
            for line in order.order_line:
                to_be_invoiced  += line.qty_to_invoice * line.price_unit

        if (credit - debit + to_be_invoiced + self.amount_total) > partner.credit_limit:
            if not partner.over_credit:
                msg = '%s has a Credit Limit of %s.\n\n ' \
                      'Value of this Order: %s.\n' \
                      'Credit Used from prior Orders: %s. **\n '\
                      'Prior Orders yet to be Invoiced: %s.\n\n' \
                      'No further Orders can be placed unless the Credit Limit is increased or relaxed. \n\n' \
                      '** Open Invoices minus Open Credits minus Unapplied Payments.' \
                      % (partner.name,'${:,.2f}'.format(partner.credit_limit),'${:,.2f}'.format(self.amount_total), '${:,.2f}'.format(credit-debit),'${:,.2f}'.format(to_be_invoiced))
                raise UserError(_('Credit Limit Reached!\n\n' + msg))
            partner.write(
                    {'credit_limit': credit - debit + self.to_be_invoiced })
        return True

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            order.check_limit()
        return res

    @api.constrains('amount_total')
    def check_amount(self):
        for order in self:
            order.check_limit()
