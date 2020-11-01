# Notes


## Doc_Bulk

### 2 check:
- not dir in year/mon/date/org level
- bad <date> folder name
- not file in last level
- not pdf

### Responses:

| Uw | Cod | Desc | Used |
|----| --- | ---- | ---- |
| ++ | 201 | Created | Doc created
| -+ | 207 | Multistatus | (partialy created)
| -+ | 400 | Bad Request | 4. bad date
| ++ | 404 | Not found | 3. Shipper not found
| ++ | 405 | Method not allowed | 1. !POST
| ++ | 406 | Not Acceptable | 2. Few data (shipper/org/date/file[s])
| -+ | 409 | Conflict | [File] already exists
| -+ | 413 | Request entity too large | *File too large*
| -+ | 415 | Unsupported Media Type | Not pdf
| -+ | 500 | Internal server error | Org/File/Doc not created
| == | === | === | ===
| -? | 200 | OK | (object uri in response)
| +? | 204 | No Content | like 'no comments' ~~(no one doc created)~~
| -- | 403 | Forbidden | request ok but operation not permited
| -- | 410 | Gone | resource deleted
| +- | 412 | Precondition failed | IfMatch not meet
| -- | 422 | Unprocessable entity | (webdav) request ok but logical error
| -- | 428 | Precondition Required | (try update not fresh resource copy)

* Uw - Used, will use

Results (4xx/5xx):
- all created (empty): 201 [w/ urls]
- not all created (207 w/ errs)
- 0 created (207 w/ errs)

### Django responses
- ~~304~~ HttpResponseNotModified
- 400 HttpResponseBadRequest
- ~~403~~ HttpResponseForbidden
- 404 HttpResponseNotFound
- 405 HttpResponseNotAllowed
- ~~410~~ HttpResponseGone
- 500 HttpResponseServerError

### Usual:
- [Powered by](https://stackoverflow.com/questions/18051407/update-queryset-in-django-in-following-situation/18052834)
- [Enum](https://docs.python.org/3/library/http.html#http.HTTPStatus)
- [207](https://evertpot.com/http/207-multi-status)

## CSS
- type
- .class
- #id
- [attr-value]
- a,b: a | b
- a b: b in a
- a>b: b right in a
- a~b: b after a in same parent in same level
- a+b: ...

## Views:
- View () - just get(), post()
- FormView (generic.edit) - form
- TemplateView (generic)
- RedirectView (?)
- ListView (generic) - model
- CreateView (generic.edit) - model+form
- DetailView (generic) - model
- UpdateView (generic.edit) - model+form
- DeleteView (generic.edit) - model

## Icons
[Search](https://www.amp-what.com/unicode/search/home)
[Explore](https://www.toptal.com/designers/htmlarrows/)
[Test](https://mothereff.in/html-entities)
- &#9993; Email
- &#9940; Stop
- &#9888; Warning
- &#9786; Smile
- &#9000; Keyboard

## Doc types:
- Счет
- Счет-фактура
- Товарная накладная
- Товарно-транспортная накладная
- Качественное удостоверение
- Сертификат качества
- Декларация соответствия
- &hellip;

## Fixtures:
[RTFM](https://docs.djangoproject.com/en/3.0/howto/initial-data/)
- save: ```./manage.py dumpdata --indent 2 -o shipment_doctype.json shipment.DocType```
- load: ```./manage.py loaddata shipment_doctype.json```

## Usual
- [Sort table](https://www.kryogenix.org/code/browser/sorttable/)
