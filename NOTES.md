# Notes

## CSS
- type
- .class
- #id
- [attr-value]
- a,b: a | b
- a b: b in a
- a>b: b right in a
- a~b: - b after a in same parent in same level
- a+b: - 

CSS online editor:
- https://cssdeck.com/labs
- http://www.cssdesk.com
- https://www.w3schools.com/tryit/
- https://codepen.io/

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

## Doc types:
- Счет
- Счет-фактура
- Товарная накладная
- Товарно-транспортная накладная
- Качественное удостоверение
- Декларация соответствия
- &hellip;

## Fixtures:
[RTFM](https://docs.djangoproject.com/en/3.0/howto/initial-data/)
- save: ```./manage.py dumpdata --indent 2 -o shipment_doctype.json shipment.DocType```
- load: ```./manage.py loaddata shipment_doctype.json```
