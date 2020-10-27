"""
Custom template tags.
[Rtfm](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
TODO: filter, org, doc, file
Future: sort (asc/desc)
"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

buttons_items = {  # key: (symbol, tip)
    'ok': ('&check;', 'OK'),
    'no': ('&olarr;', _('Cancel')),
    'add': ('&plus;', _('New')),  # &plus
    'del': ('&cross;', _('Delete')),  # &#9249;
    'del*': ('&cross;', _('Delete selected')),  # &#9249;
    'edit': ('&#9998;', _('Edit')),
    'edit*': ('&#9998;', _('Edit selected')),
    'beg': ('&larrb;', _('Start')),  # &#9194;
    'prev': ('&larr;', _('Previous')),  # &#9198;
    'next': ('&rarr;', _('Next')),  # &#9197;
    'end': ('&rarrb;', _('End')),  # &#9193;
    'dl': ('&DownArrowBar;', _('Download')),
    'show': ('&gtdot;', _('View')),  # &#128065; (eye)
    'home': ('&#8962;', _('Home')),  # svgbutton/home.html
    'tool': ('&#9881;', _('Admin')),  # svgbutton/admin.html
    'info': ('&#8505;', _('About')),  # &#9432;
    'lin': ('&rdsh;', _('Log in')),
    'lout': ('&lsh;', _('Log out')),
    'filt': ('&nabla;', _('Filter')),  # &yen;
    'file': ('&#128206;', _('File')),  # &#10064; (cubes) / svgbutton/file.html
    'doc': ('&#128214;', _('Document')),  # &# 128203 (clip), 9993; (envelop), 9997; (hand) / svgbutton/book.html
    'org': ('&#127970;', _('Organisation')),  # svgbutton/org.html
}

register = template.Library()


@register.inclusion_tag('tags/button.html')
def button(key):
    img, title = buttons_items.get(key, ('?', '---'))
    return {
        'img': mark_safe(img),
        'title': title,
    }


@register.inclusion_tag('tags/submit.html')
def submit(key, action=''):
    img, title = buttons_items.get(key, ('?', '---'))
    return {
        'img': mark_safe(img),
        'title': title,
        'action': action
    }
