"""
Custom template tags.
[Rtfm](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
[entities](https://www.amp-what.com/unicode/search/home):
- &  # 8962; Home
- &  # 9993; email
- &  # 9940; stop
- &  # 9888; warning
"""
from django import template
from django.utils.safestring import mark_safe

buttons_items = {
    'ok': ('&check;', 'OK'),
    'no': ('&cross;', 'Cancel'),
    'add': ('&plus;', 'Add'),
    'del': ('&#9249;', 'Delete'),
    'edit': ('&#9998;', 'Edit'),
    'beg': ('&#9194;', 'Start'),
    'prev': ('&#9198;', 'Previous'),
    'next': ('&#9197;', 'Next'),
    'end': ('&#9193;', 'End'),
    'dl': ('', ''),
    'show': ('', ''),
    '': ('', ''),
}

register = template.Library()


@register.inclusion_tag('tags/button.html')
def button(btype):
    # print("Button tag:", btype)
    img, title = buttons_items.get(btype, ('?', '---'))
    return {
        'img': mark_safe(img),
        'title': title
    }
