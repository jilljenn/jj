# -*- coding: utf-8 -*-
"""
    ReST directive for embedding Isso comments.

    Example::

        .. isso-comments::

    :copyright: (c) 2015 by Jill-Jênn Vie
    :license: Pas encore choisi
"""
from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class IssoComments(Directive):
    html = '<script data-isso-lang="%(lang)s" data-isso="//comments.jiji.cat/jj/" \
    src="//comments.jiji.cat/jj/js/embed.min.js"></script> \
    <section id="isso-thread"></section>'
    # has_content = False
    required_arguments = 1
    # optional_arguments = 0
    # final_argument_whitespace = False

    def run(self):
        self.options['lang'] = self.arguments[0]
        return [nodes.raw('', self.html % self.options, format='html')]


def setup(builder):
    directives.register_directive('isso-comments', IssoComments)
