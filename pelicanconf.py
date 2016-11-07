#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ljubljana Pyramid Hackers'
SITENAME = u'A full week of sprinting on Pyramid'
SITESUBTITLE = u'5 to 9 December 2016, set in the beautiful Ljubljana, Slovenia'
SITEURL = 'http://dragonsprint.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

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
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = "../themes/backdrop"
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PLUGIN_PATH = '../plugins'
PLUGINS = [
    'representative_image',
]
