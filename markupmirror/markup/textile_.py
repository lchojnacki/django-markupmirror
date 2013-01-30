from django.utils.translation import ugettext_lazy as _

from markupmirror import settings
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class TextileMarkup(BaseMarkup):
    """Markup transformer for `Textile`_ content.

    .. _Textile: http://www.textism.com/tools/textile/

    """
    codemirror_mode = 'text/plain'
    title = _(u"Textile")
    requires = ("textile.textile", )

    def __init__(self):
        self.textile_settings = settings.MARKUPMIRROR_TEXTILE_SETTINGS
        self.textile = self.required['textile']

    def convert(self, markup):
        return self.textile(markup, **self.textile_settings)

__all__ = ('TextileMarkup',)
