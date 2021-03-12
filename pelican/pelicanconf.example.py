#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from emojiextension import EmojiExtension


########################################
# Settings
########################################
DELETE_OUTPUT_DIRECTORY = True
SITEURL = 'http://thecaligarmo.com/dev/pelican' # ensure it matches output in Makefile

THEME = 'theme/thecaligarmo'
AUTHOR = u'thecaligarmo'

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u'en'

MARKDOWN = {
        'extensions' : [
            'extra',
            EmojiExtension.create_from_json('./resources/emojis.json')
            ],
        'extension_configs': {
            'markdown.extensions.extra': {},
            },
        'output_format': 'html5',
        }

STATIC_PATHS = ['images', 'css', 'js']

# FAVICON = 'images/favicon.ico'
# FAVICON16
# FAVICON32
# FAVICON48
# FAVICON96
# FAVICON_IE
# TOUCHICON


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#################
# Plugins
#################
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
PLUGIN_PATHS = ['/srvrWeb/pelican/pelican-plugins']
PLUGINS = ['i18n_subsites', 'dateish', 'tipue_search','pelican.plugins.more_categories']
# 'liquid_tags.gram',

#### i18n_subsites
#### - Allows translations
JINJA_ENVIRONMENT = {'extensions' : ['jinja2.ext.i18n']}
#I18N_TEMPLATES_LANG = 'en'
I18N_UNTRANSLATED_ARTICLES = 'keep'
I18N_UNTRANSLATED_PAGES = 'keep'

#### dateish
#### - Allows custom meta data to be treated like dates
# DATEISH_PROPERTIES = []

#### Google Analytics
# GOOGLE_ANALYTICS = 'G-FSPS9B62P7'

#### Disqus
#DISQUS_SITENAME = ''
#DISQUS_NO_ID = ''

#### Tipue Search
TIPUE_SEARCH = True

#################
# Styling
#################
FONT_CSS = '<link href="https://fonts.googleapis.com/css?family=Amiri&display=swap" rel="stylesheet">'
FONT_FAMILY = "font-family: 'Amiri', serif;"

# CUSTOM_CSS = ''

#################
# Colors
#################
# https://mycolor.space/
# Use Shades
# and
# maketintsandshades.com
#################
BACKGROUND_COLOR = '#f1f6f8'
MAIN_COLOR = '#357F9B' # Main color
SECONDARY_COLOR = '#A7ECFF'
LINK_COLOR = '#357F9B'
LINK_HOVER_COLOR = '#5399B6'

#################
# Header
#################
HEADER_IMAGE = False
HEADER_LOGO = False

#################
# Feed information
#################
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#################
# Navigation
#################
MENUITEMS = (('Home', SITEURL),)
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

CATEGORY_SAVE_AS = '{slug}.html'
CATEGORY_URL = '{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}.html'

ARTICLE_SAVE_AS = os.path.join('{category}', '{slug}.html')
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = os.path.join('{category}', '{slug}.html')
ARTICLE_LANG_URL = '{category}/{slug}.html'

#################
# Footer
#################
FOOTER_LEFT_MENU = (('Home','http://thecaligarmo.com/'),)
FOOTER_MIDDLE_MENU = (('IG','http://instagram.com'),)
# FOOTER_RIGHT_MENU = ()
COPYRIGHT = '&copy; 2020'

#################
# Pagination
#################
DEFAULT_PAGINATION = False
#DEFAULT_PAGINATION = 10
#PAGINATION_PREVIOUS = '<'
#PAGINATION_NEXT = '>'

import sys
sys.path.append('.')
from textconf import *

from fr_langconf import SUBSITE_FR

I18N_SUBSITES = {
        'fr': SUBSITE_FR
        }
