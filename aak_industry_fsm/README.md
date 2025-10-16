# AAK Industry FSM Module v18.0

This module provides an easy way to manage Field Service tasks, allowing customers to respond to scheduled visit date requests via a simple Yes/No button in an email. It integrates with the Odoo Project Management and Field Service (Industry FSM) modules.

## Features
- Customers can respond to planned service visit dates via email using Yes/No buttons.
- Responses are logged in the task's chatter, and task assignees are notified.
- A thank-you page is rendered after customer response.
- Field Service tasks send automatic email notifications for scheduled visit dates.

## Installation

1. Install this module from the Odoo App Store or manually by placing it in your Odoo `addons` directory.
2. Activate the module in Odoo.

## Configuration

No additional configuration is required.

## Dependencies

This module depends on the following modules:
- `industry_fsm`: The Odoo Field Service Management module.
- `mail`: Odoo’s email handling module.

## Usage

1. When a task is created with a planned end date, the system will automatically send an email to the customer asking for confirmation of availability.
2. The customer can respond by clicking the `Yes` or `No` button in the email.
3. The response is logged in the task chatter, and an email notification is sent to the task assignees.
4. After responding, the customer sees a thank-you page confirming their response.

## Contact

For support and inquiries, please contact us at:
- Email: office@aakoryx.com
- Website: [AAKORYX](https://www.aakoryx.com)

## Maintainer

This module is maintained by [AAKORYX](https://www.aakoryx.com).
