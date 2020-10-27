# ToDo

## ToDo:
- buttons: button_svg+submit_svg templates
- CSS (styles (positions+sizes+look)/colors)
- doc_bulk: verbose x 2 (prepare, upload)

## FixMe:
- Doc.create: blank comments
- Doc.edit: doctype required=True
- DocList.filter: date year is in future only; must be from db
- view.*_* => forms.View (file_get, file_show, org_delete_multi, doc_delete_multi, doc_bulk)
- Org: full name -> Notes
- Doc: Comments -> Notes
- File: create() with crc(md5) and/or mime
- File: chk crc on creation
- mime on 1st block (1KB?) or chunk
- Doc.add: validate all of files (form_valid())
- File.admin: disable edit on add
- Doc.admin: no add, edit w/o file (!editable=False)

## Features:
- Preview pane
- Sort
- Keyboard navigation (arrows, Ins, Del, Enter, Space)
- Multicolumn lists (grid view?)
- Inplace edits
- "2 del?" - in-place/popup
- File: chk crc on file upload
- File: chk size on upload
- File.crc - 64bit ([Positive]BigIntegerField; SipHash; python: builtin hash(), python3-siphash; cli - )
- DocList date-based views [lists](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-date-based/)
- mime &rarr; - separate model (signature; ext, name) and/or inner dict()
- mime: +icon
- preview: img cache (grey)
- icons: awesome font?
- idea: email docs
- tests
- Merge Orgs (option; can multiedit)
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
- Doc: Multiple edit (shipper, org, date, doctype)
- Filters: shipper, org, date, doctype
- fixed: mime == application/x-empty
- fixtures (NOTES.md)
- i18n
- button.symbols: login, logout, filter, org, doc, file etc
- submit button tag
