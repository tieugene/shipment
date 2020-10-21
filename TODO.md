# Shipment

## ToDo:
- Doc: bulk upload via CLI (curl)
  option: multiple files at once

## FixMe:
- mime on 1st block (1KB?) or chunk
- MD5 is strange
- Doc.add: validate all of files
- File.admin: disable edit on add
- Doc.admin: no add, edit w/o file (!editable=False)

## Features:
- Fixtures
- "2 del?" - in-place/popup
- Delete multiple (checked)
- CRC: chk on file upload
- File.crc - 64bit ([Positive]BigIntegerField; SipHash; python: builtin hash(), python3-siphash; cli - )
- Chk file size on upload
- DocList date-based views [lists](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-date-based/)
- mime &rarr; - separate model (signature; ext, name) and/or inner dict()
- preview cache (grey)
- awesome font? for icons
- idea: multicolumn = grid view
- idea: email docs
- tests
- Buttons - text + html [entities](https://www.amp-what.com/unicode/search/home)
  (as [template tag](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
  for [&lt;button&gt;](http://htmlbook.ru/html/button)):
  - &#8962; Home
  - &check; OK
  - &cross; Cancel
  - &plus; Add
  - &#9249; Delete
  - &#9998; Edit
  - &#9198; Prev / &#9197; Next
  - &#9194; Left / &#9193; Right
  - &#9993; email
  - &#9940; stop
  - &#9888; warning

### Done:
- Org CRUDLa
- Shipper: admin only
- DocType: admin only
- File: CRUDLa
- File: id-based name
- Doc: CRUDL
- Doc: pdf only
- File/Doc: download/preview ok
- File: list - show doc
- Doc.del: del File (and vice versa)
- FormView instead of *_add
- Doc multiple upload (set defaults: shipper, org, date[, doctype][, comments]):
  [builtin](https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/#uploading-multiple-files)
- big files upload ok (they are TemporaryUploadedFile)
