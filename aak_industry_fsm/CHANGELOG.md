# Changelog
All notable changes to this project will be documented in this file.

## [18.0.1.0.0] - 2025-10-09 | Initial Release
### Features:
- Added HTTP endpoint to collect simple Yes/No responses from customers for Field Service tasks.
- Logs customer responses in the task's chatter.
- Notifies task assignees with an email template when a response is received.
- Renders a thank-you page after the customer submits their response.

### Dependencies:
- Odoo `industry_fsm` (Field Service Management).
- Odoo `mail` module for email notifications.
