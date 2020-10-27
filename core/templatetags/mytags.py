"""
Custom template tags.
[Rtfm](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)
TODO: filter, org, doc, file
Future: sort (asc/desc)
"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

buttons_items = {  # key: (char, img, tip)
    'ok': ('&check;', 'check', 'OK'),
    'no': ('&olarr;', 'ban', _('Cancel')),
    'add': ('&plus;', 'plus', _('New')),  # &plus
    'del': ('&cross;', 'trash-o', _('Delete')),  # &#9249;
    'del*': ('&cross;', 'plus', _('Delete selected')),  # &#9249;
    'edit': ('&#9998;', 'pencil', _('Edit')),
    'edit*': ('&#9998;', 'pencil', _('Edit selected')),
    'beg': ('&larrb;', 'fast-backward', _('Start')),  # &#9194;
    'prev': ('&larr;', 'step-backward', _('Previous')),  # &#9198;
    'next': ('&rarr;', 'step-forward', _('Next')),  # &#9197;
    'end': ('&rarrb;', 'fast-forward', _('End')),  # &#9193;
    'dl': ('&DownArrowBar;', 'download', _('Download')),
    'show': ('&gtdot;', '0014-image', _('View')),  # &#128065; (eye)
    'home': ('&#8962;', 'home', _('Home')),
    'tool': ('&#9881;', 'cog', _('Admin')),
    'info': ('&#8505;', 'info', _('About')),  # &#9432;
    'lin': ('&rdsh;', 'sign-in', _('Log in')),
    'lout': ('&lsh;', 'sign-out', _('Log out')),
    'filt': ('&nabla;', 'filter', _('Filter')),  # &yen;
    'file': ('&#128206;', 'file-o', _('File')),  # &#10064; (cubes)
    'doc': ('&#128214;', 'book', _('Document')),  # &# 128203 (clip), 9993; (envelop), 9997; (hand)
    'org': ('&#127970;', 'industry', _('Organisation')),
}

register = template.Library()


# HTML entity powered
@register.inclusion_tag('tags/button.html')
def button(key):
    char, img, title = buttons_items.get(key, ('?', None, ''))
    return {
        'char': mark_safe(char),
        'title': title,
    }


@register.inclusion_tag('tags/submit.html')
def submit(key, action=''):
    char, img, title = buttons_items.get(key, ('?', None, '---'))
    return {
        'char': mark_safe(char),
        'title': title,
        'action': action
    }


# SVG powered
@register.inclusion_tag('tags/button_svg.html')
def button_(key):
    char, img, title = buttons_items.get(key, ('?', 'usd', '---'))
    return {
        'path': "img/svg/{}.svg".format(img),
        'title': title,
    }


@register.inclusion_tag('tags/submit_svg.html')
def submit_(key, action=''):
    char, img, title = buttons_items.get(key, ('?', 'usd', '---'))
    return {
        'path': "img/svg/{}.svg".format(img),
        'title': title,
        'action': action
    }
