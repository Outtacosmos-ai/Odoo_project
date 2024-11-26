{
    "name": "Custom Stock Picking",
    "version": "11.0.1.0.0",
    "author": "Sultan",
    "category": "Inventory",
    "summary": "Enhanced Stock Picking State Management",
    "description": """
        Custom Stock Picking module with additional features:
        - Set to Draft button in Transfers
        - Enhanced state management
        - State transitions between Draft, Waiting, Ready, Done
    """,
    "depends": ["stock"],
    "data": [
        "security/stock_picking_security.xml",
        "views/stock_picking_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
