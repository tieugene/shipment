# Shipment

## ToDo:
- Filters: date, shipper, org, doctype
- Paginator
- Bulk upload prepare (python walk() &rarr; curl)
- Multiple del (&#9744; &#9745;)
- Multiple edit
- Merge orgs
- [Fixtures](https://docs.djangoproject.com/en/3.1/howto/initial-data/)
- view.*_* => forms.View
- Interface:
  - CSS
  - icons: preview, download, doc exists
  - i18n

## FixMe:
- mime: application/x-empty
- File: chk crc on creation
- File: create() with crc(md5) and/or mime
- mime on 1st block (1KB?) or chunk
- Doc.add: validate all of files
- File.admin: disable edit on add
- Doc.admin: no add, edit w/o file (!editable=False)

## Features:
- "2 del?" - in-place/popup
- File: chk crc on file upload
- File: chk size on upload
- File.crc - 64bit ([Positive]BigIntegerField; SipHash; python: builtin hash(), python3-siphash; cli - )
- DocList date-based views [lists](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-date-based/)
- mime &rarr; - separate model (signature; ext, name) and/or inner dict()
- preview: img cache (grey)
- icons: awesome font?
- idea: multicolumn = grid view
- idea: email docs
- tests
- [WebDAV](https://github.com/MnogoByte/djangodav)
- pylint with [pylint-django](https://github.com/PyCQA/pylint-django)

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
- buttons as template tags
- Doc: bulk upload via CLI (curl)
- MD5

## icons
[Search](https://www.amp-what.com/unicode/search/home) or
[Explore](https://www.toptal.com/designers/htmlarrows/)
[Test](https://mothereff.in/html-entities)
- &#8962; Home
- &#9993; Email
- &#9940; Stop
- &#9888; Warning
- &#9786; Smile
- &#9874;&#9881; Tools
- &#9000; Keyboard
- &#128269; ~~Magnify~~
- &#128065; ~~Eye~~
- &#128424; ~~Print~~
