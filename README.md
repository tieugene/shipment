# Shipment

## Requires:
- django
- python-magic

## Tools:
- Django
- [WebDAV](https://github.com/MnogoByte/djangodav)
- pylint with [pylint-django](https://github.com/PyCQA/pylint-django)

## Classes
- core:
  - File
  - [Mime]
- shipment:
  - DirTree
  - Org
  - Partner
  - Document

## Actions
- CRUD
- Search
- Filter (year[-mon[-date]], Partner, Owner)
- merge Partners
- change history

## Utility
- sync/import with local files:
  - Year &rarr; Month &rarr; dd.mm.yyyy &rarr; partner
  - show not imported
  - show new
  - chk crc64
