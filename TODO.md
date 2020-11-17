# ToDo

## 201117:
ConfirmDeleteMulti.

Variants:
- view.get(): replace FormView.get(), template: form method=get
- forward: POST=>FormView.is_valid()=>redirect ConfirFormView.get()

## FixMe:
- view.*_* => forms.View (*_delete_multi, doc_bulk)
- multi_del: confirm delete form (File, Org, Doc)
- *.Edit: return to ~~detail~~ referrer
- highlight whole tr:hover
- Org: full name -> Note
- Doc: Comments -> Note
- File: create() with crc(md5) and/or mime
- File: chk crc on creation
- Doc.add: validate all of files (form_valid())
- File.admin: disable edit on add
- Doc.admin: no add, edit w/o file (!editable=False)
- File upload: preserve ctime ('Last-Modified', 'creation-date')

## Features:
- DocList.filter: y/m/d from db
- model.field, readonly
- tests
- auth
- File trashcan
- journal (CRUDL, RRD?)
- File.ctime: use source (=> teach attachment attrs)
- [multi]edit: replace POST with PUT(==UPDATE)|PATCH
- [multi]del: replace with DELETE
- icons: fileS, orgS, docS, delS, editS
- Preview pane
- Sort
- button style by name="" attr
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
- buttons: button_svg+submit_svg templates
- CSS (position, size, decoration, color; even/odd tr)
- buttons: kwargs (e.g. disabled)
- doc_bulk: self upload + verbose x 2 (prepare, upload)
- doc_bulk: python/curl client works ok
- Fixed: Org.add(): fullname required
- Fixed: Doc.create: blank comments
- Fixed: Doc.edit: doctype required=True (blank=True)
- apache ready
- mime on 1st block (1KB)
- date filter: separate yy/mm/dd
- DocMultiEdit: future years only fixed
- Sorting (File/Doc x asc/desc). Session keys: <model>_sort='[-]field'
- merge organisations
