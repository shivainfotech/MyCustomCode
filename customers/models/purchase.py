# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from openerp import api, fields, models, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

	
    partner_ref1 = fields.Char(string='Partner ref', copy=False)
	
# class PurchaseOrder(models.Model):
#     _inherit='purchase.order'


# 	#test_id=fields.Many2one('res.partner',string='testing')
    

# class PurchaseMove(models.Model):
#     _inherit = 'purchase.order.line'

#     @api.multi
#     def button_confirm(self):
#         res = super(PurchaseMove, self).action_confirm()
#         for move in self:
#             if  move.order_id and move.partner_ref:
#                 move.partner_ref = move.partner_ref
#         return res
