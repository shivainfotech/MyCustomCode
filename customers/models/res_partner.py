# -*- coding: utf-8 -*-

from openerp import models,api,fields,_


class ResPartner(models.Model):
	_inherit = 'res.partner'

	customer_id = fields.Char(string="Customer ID", required=True)
	
	