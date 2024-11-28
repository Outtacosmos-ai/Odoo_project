from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    @api.multi
    def button_set_to_draft(self):
        """
        Optimized function to cycle through states:
        draft -> confirm (in progress) -> done (validated) -> draft
        """
        for record in self:
            if record.state == 'draft':
                record.action_start()
            elif record.state == 'confirm':
                record.action_validate()
            elif record.state == 'done':
                record.write({'state': 'draft'})
            else:
                record.write({'state': 'draft'})
        return True
