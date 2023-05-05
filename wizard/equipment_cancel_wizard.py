from odoo import models, fields, api,_


class EquipmentCancel(models.TransientModel):
    _name = 'equipment.cancel'
    _description = "Equipment Cancel"


    my_bool = fields.Boolean(string ='My Boolean')

    def action_cancel(self):
        active_ids = self.env.context.get('active_ids')
        equipment = self.env['equipment'].browse(active_ids)
        for equip_ids in equipment:
            equip_ids.move_one_step_back()

    # order_id = fields.Many2one('equipment', string='Equipment', required=True, ondelete='cascade')
    # display_invoice_alert = fields.Boolean('Invoice Alert', compute='_compute_display_invoice_alert')

    # @api.depends('order_id')
    # def _compute_display_invoice_alert(self):
    #     for wizard in self:
    #         wizard.display_invoice_alert = bool(wizard.order_id.invoice_ids.filtered(lambda inv: inv.state == 'draft'))

    # def action_cancel(self):
    #     return self.order_id.with_context({'disable_cancel_warning': True}).action_cancel()
