# -*- coding: utf-8 -*-

from openerp import models,api,fields,_



class PurchaseOrder(models.Model):
	_inherit ="purchase.order"

	customer_id = fields.Char(related="partner_id.customer_id",store=True)

	#purchase_ref= fields.Char( string='partner ref')

	# test_id=fields
#testing
