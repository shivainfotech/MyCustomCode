# -*- coding: utf-8 -*-

from openerp import models,api,fields,_


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	customer_id = fields.Char(related="partner_id.customer_id", store=True)

	#mycustom_res=fields.Many2one()
	partner_id1 = fields.Many2one('res.partner', string="partner_id")
	mycustom =fields.Char()