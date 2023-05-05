from odoo import models, fields, api


class ResPartern(models.Model):
    _inherit = 'res.partner'


    is_employee = fields.Boolean(String="Is Employee")
