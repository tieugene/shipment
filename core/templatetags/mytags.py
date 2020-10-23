"""
Custom template tags.
[Rtfm](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
"""
from django import template
from django.utils.safestring import mark_safe

buttons_items = {
    'ok': ('&check;', 'OK'),
    'no': ('&cross;', 'Cancel'),
    'add': ('&oplus;', 'Add'),           # &plus
    'del': ('&otimes;', 'Delete'),       # &#9249;
    'edit': ('&#9998;', 'Edit'),
    'beg': ('&#9194;', 'Start'),        # &larrb;
    'prev': ('&#9198;', 'Previous'),    # &larr;
    'next': ('&#9197;', 'Next'),        # &rarr;
    'end': ('&#9193;', 'End'),          # &rarrb;
    'dl': ('&DownArrowBar;', 'Download'),
    'show': ('&gtdot;', 'View'),
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
