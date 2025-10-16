# Changelog
All notable changes to this project will be documented in this file.

## [18.0.1.0.0] - 2025-10-09 | Initial Release
### Added
- First-time release of the AAK CRM Customer Feedback module.
- **CRM Lead Activity**: Automatically creates daily activities for newly created leads.
- **Customer Feedback Survey**: Sends an automated email with a personalized survey link after a stock picking is validated.
- **Survey Questions**:
    - Service satisfaction
    - Installation quality
    - Safety compliance
    - Timeliness of installation
- **Cron Job**: A cron job is scheduled to create follow-up activities for CRM leads created that day.

### Fixed
- No issues, as this is the initial release.

### Improvements
- Simple, effective integration with CRM leads and stock picking.
- The module ensures that customer feedback is collected after deliveries, helping improve service quality.
- 
## [18.0.1.1.0] - 2025-10-14 | Update
### Changed
- **Customer Feedback Survey Trigger**: The survey is now sent when the related **Project Task** is marked as done instead of when the stock picking is validated.

### Improvements
- Aligns feedback collection with task completion, allowing more accurate customer experience tracking.

## [18.0.1.2.0] - 2025-10-16 | Update
### Added
- **New Survey Questions**: Added new survey questions for customer feedback:
  - What could we do to improve your overall experience?
  - What additional solutions would you like more information about?
  - Choices for additional solutions include:
    - Alarm Systems
    - Video Surveillance
    - Access Control
    - Fire Detection
    - Monitoring Services
  - These questions are now included in the "Customer Satisfaction Survey."

### Changed
- **Project Task FSM Validation**: Refined the logic for determining the service type (`security`, `two_way_radio`), and dynamically selecting the corresponding survey.

### Improvements
- Enhanced the customer feedback survey to gather more actionable insights about the services provided.
- Improved the task validation process by simplifying the service type-based survey selection logic.