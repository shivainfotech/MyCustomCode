# -*- coding: utf-8 -*-

from openerp import models,api,fields,_


class ResPartner(models.Model):
	_inherit = 'product.template'

	map_price = fields.Char(string="Map Price", required=True)