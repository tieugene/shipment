# Shipment

General purpose file storage with addition functionality for shipping documents archiving.

## Features
- Shipping documents have attributes to filter and sort:
  - Own organization
  - Partner
  - Document (shipping) date
  - Document type (orders, bills, invoices etc)
- Bulk uploading documents
- Uploading document type restriction (PDF only)

## Requires
- Python 3.x
- Django
- Python-magic
- Django-compatible RDB backend (SQLite, MariaDB, PostgreSQL etc)
