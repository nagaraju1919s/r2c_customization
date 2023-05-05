from odoo import models, fields, api,_

class Equipment(models.Model):
    _name = 'equipment'
    _inherit = ["mail.thread", "mail.activity.mixin"]


    status_bar = fields.Selection([('draft', 'Draft'),('waiting for approval', 'Waiting For Approval'),('approved','Approved')],default='draft', String="Status")
    machine_name = fields.Char('Machine Name')
    checking = fields.Selection([('n','working'),('w','notworking')],String = "Machine checking")
    product_id = fields.Many2one('product.template',"Product")
    count = fields.Integer()
    dob = fields.Date(String="Date Of Existance", tracking=True)
    default_code = fields.Char(related='product_id.default_code')
    equipment_line_ids = fields.One2many('equipment.line','equipment_id',String="Purchase")
    total_cost = fields.Float(String="total_cost", compute='_compute_total_cost')

    def send_approval(self):
        for rec in self:
            rec.status_bar='waiting for approval'
        
    def wait_approval(self):
        for rec in self:
            rec.status_bar='approved'

    def move_one_step_back(self):
        for rec in self:
            rec.status_bar='draft'

    def _compute_total_cost(self):
        sum=0
        for i in self.equipment_line_ids:
            sum= sum+i.cost
        self.total_cost = sum

    def cancle(self):
        # cancel_warning = self._show_cancel_wizard()
        # if cancel_warning:
        return {
            'name': _('Cancel Equipment'),
            'view_mode': 'form',
            'res_model': 'equipment.cancel',
            'view_id': self.env.ref('test1.equipment_cancel_cancel_view_form').id,
            'type': 'ir.actions.act_window',
            # 'context': {'default_order_id': self.id},
            'target': 'new'
        }
        return self.cancle()




class EquipmentLine(models.Model):
    _name = 'equipment.line'

    equipment_id = fields.Many2one('equipment',string='Equipment')
    purchase_order_id = fields.Many2one('purchase.order','Purchase_order')
    product_id = fields.Many2one('product.template','Product')
    no_of_purchase = fields.Float('No.Of.Purchase')
    uom_po_id = fields.Many2one(related='product_id.uom_po_id')
    cost = fields.Float()