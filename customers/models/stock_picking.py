# -*- coding: utf-8 -*-

from openerp import models,api,fields,_



class StockPicking(models.Model):
	_inherit ="stock.picking"

	customer_id = fields.Char(related="partner_id.customer_id", store=True)

    
	
'''
class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_confirm(self):
        res = super(StockMove, self).action_confirm()
        for move in self:
            if move.procurement_id and move.procurement_id.sale_line_id and move.procurement_id.sale_line_id.order_id.incoterm:
                move.picking_id.incoterm = move.procurement_id.sale_line_id.order_id.incoterm
        return res
'''	

	
# testing purpose
 


	 

