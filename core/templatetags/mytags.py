"""
Custom template tags.
[Rtfm](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

buttons_items = {   # key: (symbol, tip)
    'ok': ('&check;', 'OK'),
    'no': ('&cross;', _('Cancel')),
    'add': ('&plus;', _('New')),           # &plus
    'del': ('&cross;', _('Delete')),       # &#9249;
    'edit': ('&#9998;', _('Edit')),
    'beg': ('&larrb;', _('Start')),        # &#9194;
    'prev': ('&larr;', _('Previous')),    # &#9198;
    'next': ('&rarr;', _('Next')),        # &#9197;
    'end': ('&rarrb;', _('End')),          # &#9193;
    'dl': ('&DownArrowBar;', _('Download')),
    'show': ('&gtdot;', _('View')),
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
