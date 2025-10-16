AAK Fleet Extension
===================

This module extends the `fleet.vehicle` model to include additional fields like:
- Vehicle ID (auto-generated)
- Customer (Many2one `res.partner`)
- Make (Many2one `fleet.vehicle.model.brand`)
- Previous Installations (Text field)
- Radio Model (Char field)
- Installation Location (Char field)
- Antenna Type (Char field)
- Vehicle Photos (Many2many `ir.attachment`)

Dependencies:
-------------
* fleet (Fleet Management module)

Installation
============
Simply install this module after installing the `fleet` module.

Company:
--------
* `AAKORYX <https://www.aakoryx.com>`

Contacts:
---------
* Mail Contact: office@aakoryx.com
* Website: https://www.aakoryx.com

Bug Tracker:
-------------
For any issues or feature requests, please contact us via the provided email.

