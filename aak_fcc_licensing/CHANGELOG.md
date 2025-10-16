# Changelog
All notable changes to this project will be documented in this file.

# [18.0.1.0.0] - 2025-10-14 | Initial Release
- Added new module `AAK FCC Licensing`
- Created model `fcc.licensing` to manage FCC licenses
- Added wizard `upload.licence` to upload licenses and attach to Sale Orders
- Extended `crm.team` and `sale.order` to include FCC Licence required flag
- Added menu item "FCC Licensing" under Sales → Configuration
- Added tree and form views for FCC Licensing
- Added security access for base users

# [18.0.1.1.0] - 2025-10-16
- Updated access rights for `fcc.licensing` and `upload.licence` models to include:
    * Sale Manager
    * General Manager
    * President
- Fixed manifest to correctly load `upload_licence.xml` before views
- Removed unused `base64` import in `upload_licence.py`