""" @package TopMacro
    @file macro.py
    @brief The TopMacro class

    Return a top of page anchor element.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.1
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.api import parse_args
from genshi.builder import tag

__all__ = ['TopMacro']

class TopMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, args):
        """Return a top of page anchor element."""

        prefix  = '['
        content = '^'
        suffix  = ']'

        args, kw = parse_args(args)

        if args:
            content = args.pop(0).strip()
            prefix = suffix = ''

        # class is a python reserved identifier

        class_ = 'topofpage'
        title  = 'Top of page'

        return tag(prefix,
                   tag.a(content,
                         class_='%s' % class_,
                         href='#',
                         title='%s' % title),
                   suffix)
