# Changelog
All notable changes to this project will be documented in this file.

# [18.0.1.0.0] - 2025-09-24 | User Story #SLS-004
- New models named as component.list and product.components
- List and Form View for component.list and added menu 'Component Lists' under Sales > Configuration

# [18.0.1.0.1] - 2025-09-30 | User Story #SLS-004 #SLS-005
- Added functionality which will open wizard and user needs to fill all the details and then user is able to add components and it's list into sale.order.line
- Added functionality about 'Return Order' for equipment product while validating delivery.

# [18.0.1.0.2] - 2025-10-03 | User Story #SLS-004 #SLS-005
- Changed logic for return order of validating delivery based on sales_line.
- Fixed few bugs regarding rental and equipment product

# [18.0.1.0.3] - 2025-10-06 | User Story #SLS-004 #SLS-005
- Fixed bug regarding twice creation of return order if there is backorder or no backorder
- Changes in Return Order Quantity based on whatever we sent manually.

# [18.0.1.0.3] - 2025-10-07 | User Story #SLS-004 #SLS-005
- Fixed bug regarding validating backorders without resetting previous return quantities.

# [18.0.1.0.3] - 2025-10-10 | User Story #SLS-004 #SLS-005
- Changed name of menu and button of 'Component List' with 'BOM Inventory'.

# [18.0.1.0.3] - 2025-10-14 | User Story #SLS-004 #SLS-005
- Raised Warning if demand quantity is greater than available stock quantity.