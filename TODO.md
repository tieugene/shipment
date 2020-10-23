# ToDo

## ToDo:
- Doc: Multiple edit (shipper, org, date, doctype)
- Filters: shipper, org, date, doctype
- Merge Orgs
- [Fixtures](https://docs.djangoproject.com/en/3.1/howto/initial-data/)
- view.*_* => forms.View (file_get, file_show, doc_bulk)
- Interface:
  - CSS
  - icons: preview, download, doc exists
  - i18n

## FixMe:
- Org: full name -> Notes
- Doc: Comments -> Notes
- mime: application/x-empty
- File: chk crc on creation
- File: create() with crc(md5) and/or mime
- mime on 1st block (1KB?) or chunk
- Doc.add: validate all of files (form_valid())
- File.admin: disable edit on add
- Doc.admin: no add, edit w/o file (!editable=False)

## Features:
- Keyboard navigation (arrows, Ins, Del, Enter, Space)
- Multicolumn lists
- Inplace edits
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
- Bulk upload prepare (python walk() &rarr; curl)
- Multiple del (&#9744; &#9745;)
