#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'victal'
SITENAME = u'Free Lunch'
SITESUBTITLE = u'"There is no such thing as this site"'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/victal'),
          ('Twitter', 'http://twitter.com/g_victal'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [ 'assets','static' ]

THEME = "themes/myidea"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
