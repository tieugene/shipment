"""
Custom template tags.
[Rtfm](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
TODO: login, logout, filter,  org, doc, file
Future: sort (asc/desc)
"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


buttons_items = {   # key: (symbol, tip)
    'ok': ('&check;', 'OK'),
    'no': ('&olarr;', _('Cancel')),
    'add': ('&plus;', _('New')),        # &plus
    'del': ('&cross;', _('Delete')),    # &#9249;
    'edit': ('&#9998;', _('Edit')),
    'beg': ('&larrb;', _('Start')),     # &#9194;
    'prev': ('&larr;', _('Previous')),  # &#9198;
    'next': ('&rarr;', _('Next')),      # &#9197;
    'end': ('&rarrb;', _('End')),       # &#9193;
    'dl': ('&DownArrowBar;', _('Download')),
    'show': ('&gtdot;', _('View')),
    'home': ('&#8962;', _('Home')),     # svgbutton/home.html
    'tool': ('&#9881;', _('Admin')),    # svgbutton/admin.html
    'info': ('&#8505;', _('About')),    # &#9432;
    'lin': ('', _('Log in')),
    'lout': ('', _('Log out')),
    'filt': ('', _('Filter')),
    'file': ('', _('File')),
    'doc': ('', _('Document')),
    'org': ('', _('Organisation')),
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
