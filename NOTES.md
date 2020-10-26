# Notes

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

## Filtering:
- post: separate view; store filter into session and fw to doc_list
- get: fill form from session
- get_queryset: filter by ..?
