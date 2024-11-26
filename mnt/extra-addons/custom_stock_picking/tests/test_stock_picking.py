from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestStockPicking(TransactionCase):

    def setUp(self):
        super(TestStockPicking, self).setUp()
        self.stock_picking = self.env['stock.picking']
        self.stock_move = self.env['stock.move']
        self.product = self.env['product.product'].create({'name': 'Test Product'})
        self.location = self.env['stock.location'].create({'name': 'Test Location'})
        self.location_dest = self.env['stock.location'].create({'name': 'Test Destination Location'})

    def test_button_draft(self):
        picking = self.stock_picking.create({
            'picking_type_id': self.env.ref('stock.picking_type_internal').id,
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id,
        })
        
        move = self.stock_move.create({
            'name': 'Test Move',
            'product_id': self.product.id,
            'product_uom_qty': 1,
            'product_uom': self.product.uom_id.id,
            'picking_id': picking.id,
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id,
        })

        picking.action_confirm()
        self.assertEqual(picking.state, 'confirmed')

        picking.button_draft()
        self.assertEqual(picking.state, 'draft')
        self.assertEqual(picking.draft_count, 1)

        picking.action_done()
        with self.assertRaises(UserError):
            picking.button_draft()

    def test_multiple_draft_actions(self):
        picking = self.stock_picking.create({
            'picking_type_id': self.env.ref('stock.picking_type_internal').id,
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id,
        })

        picking.action_confirm()
        picking.button_draft()
        self.assertEqual(picking.draft_count, 1)

        picking.action_confirm()
        picking.button_draft()
        self.assertEqual(picking.draft_count, 2)

    def test_validate_draft_action(self):
        picking = self.stock_picking.create({
            'picking_type_id': self.env.ref('stock.picking_type_internal').id,
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id,
        })

        move = self.stock_move.create({
            'name': 'Test Move',
            'product_id': self.product.id,
            'product_uom_qty': 1,
            'product_uom': self.product.uom_id.id,
            'picking_id': picking.id,
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id,
        })

        picking.action_confirm()
        move.quantity_done = 1
        picking.action_done()

        with self.assertRaises(UserError):
            picking._validate_draft_action()

