{
    "name": "Custom Inventory Adjustment",
    "version": "11.0.1.0.1",
    "author": "Sultan",
    "category": "Inventory",
    "summary": "Enhanced Inventory Adjustment State Management",
    "description": """
        Custom Inventory Adjustment module with additional features:
        - Set to Draft button in Inventory Adjustments
        - Enhanced state management
        - State transitions between Draft, In Progress, and Validated
    """,
    "depends": ["stock"],
    "data": [
        "views/stock_inventory_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
