# Shipment
## todo

### Done:
- &#9745; Org CRUDLa
- &#9745; Shipper - admin only
- &#9745; DocType - admin only
- &check; File CRUDLa
- &check; File: id-based name
- &#9744; Doc - CRUDL

### Hot:
- Doc.admin: no add, edit w/o file

### file add:
- Document: chk mime on create:
  - [one](https://stackoverflow.com/questions/10923687/validate-filefield-django-as-a-valid-pdf)
  - [two](https://coderoad.ru/20761092/Как-проверить-формат-изображения-в-поле-django-ImageField)
  - [three](https://progi.pro/django-proverka-polya-fayla-v-modeli-s-ispolzovaniem-python-magic-10166178)
  - [fore](https://progi.pro/django-audio-proverka-faylov-9997753)

## Future:
- tests
- Doc bulk upload via ClI (curl)
- File.crc - 64bit (SipHash; python: builtin hash(), python3-siphash; cli - )
- admin.File - disable edit on add
- DocList date-based views [lists](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-date-based/)
- [MultiUpload](https://github.com/Chive/django-multiupload) or builtin
- Delete checked
- "select folder" on upload
- mime &rarr; - separate model (signature; ext, name) and/or inner dict()
- preview cache (grey)
- awesome font? fot icons
- idea: multicolumn = grid view
- idea: email docs
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
