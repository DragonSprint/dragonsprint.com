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
DEFAULT_CATEGORY = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sponsors & Partners
LINKS = (
    ('Python Software Foundation', 'https://www.python.org/psf/'),
    ('Termitnjak d.o.o.', 'http://www.termitnjak.com/'),
    ('Domen Kožar', 'https://www.domenkozar.com/'),
    ('NiteoWeb Ltd.', 'http://www.niteoweb.com'),
    ('Plone Foundation', 'https://plone.org/foundation'),
)

# Social widget
EMAIL = 'mailto:info@dragonsprint.com'
SOCIAL = (
    ('Github', 'https://github.com/pylons/pyramid/issues?q=is%3Aissue+is%3Aopen+label%3Asprintable'),
    ('Twitter', 'https://twitter.com/DragonSprintCom'),
    ('Meetup', 'https://www.meetup.com/Ljubljana-Python-Group/'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# GitHub custom domain support
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

# Theme
THEME = "themes/backdrop"
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PLUGIN_PATHS = ['plugins', ]
PLUGINS = [
    'representative_image',
]
BACKDROP_IMAGE = '/theme/images/backdrop.jpg'
FAVICON = '/theme/images/favicon.ico'
SITE_DESCRIPTION = 'DragonSprint is a week-long sprint on Pyramid. The sprint takes place in Ljubljana, Slovenia, EU in the first week of December (5th to 9th). The main two sprint topics are <i>Pyramid 2.0</i> and Pyramid for Newcomers. <br /><br />The sprint is <b>free</b> to attend for everyone! <a href="mailto:info@dragonsprint.com">Contact us</a> if you need help with covering your travel expenses.'
YEAR = '2016'
