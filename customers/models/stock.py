# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from openerp import api, fields, models, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'
	
    client_order_ref = fields.Char(related='sale_id.client_order_ref',string='Purchase Order', copy=False)
    mycustom =fields.Char()
    partner_id123 = fields.Many2one(related='sale_id.partner_id1',string='partner')
    purchase_refer =fields.Char( string='partner ref')

    test_ref= fields.Many2one('res.partner',string='testing')

# class StockMove(models.Model):
#     _inherit = 'stock.move'

#     @api.model
#     def _prepare_picking_assign(self, move):
#         res = super(StockMove, self)._prepare_picking_assign(move)
#         print">>>>res",res
#         res['mycustom'] = move.procurement_id.sale_line_id.order_id.mycustom
#         return res

class PurchaseOrder(models.Model):
    _inherit='purchase.order'

    @api.model
    def _prepare_picking(self):
        res =super(PurchaseOrder,self)._prepare_picking()
        res['purchase_refer'] =  self.partner_ref
        # res['test_ref']=self.test_id.id

        return res


#     @api.multi
#     def action_confirm(self):
#         res = super(StockMove, self).action_confirm()
#         for move in self:
#             if move.procurement_id and move.procurement_id.sale_line_id and move.procurement_id.sale_line_id.order_id.client_order_ref:
#                 move.picking_id.client_order_ref = move.procurement_id.sale_line_id.order_id.client_order_ref
#         return res


