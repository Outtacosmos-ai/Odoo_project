from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def button_set_to_draft(self):
        """
        Button to cycle through states:
        draft -> waiting -> ready -> done -> draft
        """
        states_cycle = ['draft', 'waiting', 'ready', 'done']
        
        for record in self:
            try:
                current_index = states_cycle.index(record.state)
                next_index = (current_index + 1) % len(states_cycle)
                next_state = states_cycle[next_index]
            except ValueError:
                next_state = 'draft'
            
            # Update move lines state
            move_state_map = {
                'draft': 'draft',
                'waiting': 'confirmed',
                'ready': 'assigned',
                'done': 'done'
            }
            
            if next_state in move_state_map:
                record.move_lines.write({'state': move_state_map[next_state]})
            
            # Update picking state
            record.write({'state': next_state})
            _logger.info('Stock picking %s state changed from %s to %s', 
                        record.name, record.state, next_state)
            
            # Additional state-specific actions
            if next_state == 'done':
                for move in record.move_lines:
                    move.quantity_done = move.product_uom_qty
            elif next_state == 'draft':
                record.move_lines.write({'quantity_done': 0.0})
        
        return True

