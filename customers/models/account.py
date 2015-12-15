# -*- coding: utf-8 -*-

from openerp import models,api,fields,_



class AccountInvoice(models.Model):
	_inherit ="account.invoice"

	customer_id = fields.Char(related="partner_id.customer_id", store=True)