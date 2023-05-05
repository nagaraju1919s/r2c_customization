from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    asset_type = fields.Selection([('in_house','In House'),('out','Out')],String="assert")