#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

from emojiextension import EmojiExtension


########################################
# Settings
########################################

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = '../public_html/dev/learning'
SITEURL = 'http://thecaligarmo.com/dev/learning'


PATH = 'content'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u'en'
MARKDOWN = {
        'extensions' : ['extra',EmojiExtension.create_from_json('./resources/emojis.json')],
        'extension_configs': {
            'markdown.extensions.extra': {},
            },
        'output_format': 'html5',
        }

# FAVICON
# FAVICON_IE
# TOUCHICON


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#################
# Plugins
#################
DIRECT_TEMPLATES = ('index','categories','authors','archives','search')
PLUGIN_PATHS = ['/srvrWeb/pelican/pelican-plugins']
PLUGINS = ['i18n_subsites', 'dateish', 'tipue_search','subcategory']

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
GOOGLE_ANALYTICS = 'G-FSPS9B62P7'

#### Disqus
#DISQUS_SITENAME = ''
#DISQUS_NO_ID = ''

#### Tipue Search
TIPUE_SEARCH = True

#### Subcategories
#PATH_METADATA= '(?P<subcategory_path>.*)/.*'

#################
# Styling
#################
FONT_CSS = '<link href="https://fonts.googleapis.com/css?family=Amiri&display=swap" rel="stylesheet">'
FONT_FAMILY = "font-family: 'Amiri', serif;"

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
LINK_COLOR = '#357F9B'
LINK_HOVER_COLOR = '#5399B6'
SECONDARY_COLOR = '#A7ECFF'
DEFINITION_COLOR = '#e5f9ff'
EXAMPLE_COLOR = '#e5f9ff'
EXAMPLE_BORDER_COLOR = '#75a5b3'

# CUSTOM_CSS = ''

#################
# Header
#################
HEADER_TITLE = 'The Cali Garmo'
HEADER_SUBTITLE = 'does Learning'
HEADER_IMAGE = False
HEADER_LOGO = False


#################
# Feed information
#################
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
SUBCATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#################
# Navigation
#################
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_PAGINATION = False


SUBCATEGORY_SAVE_AS = '{savepath}.html'
SUBCATEGORY_URL = '{fullurl}.html'

CATEGORY_SAVE_AS = '{slug}.html'
CATEGORY_URL = '{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

ARTICLE_SAVE_AS = os.path.join('{subpath}', '{slug}.html')
ARTICLE_URL = '{suburl}/{slug}.html'





########################################
# Text - Can alter for languages
########################################
AUTHOR = u'thecaligarmo'
SITENAME = u'The Cali Garmo is Learning'
SITE_DESCRIPTION = u'The Cali Garmo is Learning. Be it Maths, Languages, or Life Lessons.'
THEME = 'theme/thecaligarmo'

#################
# Navigation
#################
MENUITEMS = (('Home', SITEURL),)

#################
# Footer
#################
FOOTER_LEFT_COLUMN_TITLE = 'The Cali Garmo'
FOOTER_LEFT_MENU = (('Home','http://thecaligarmo.com/'),)
FOOTER_MIDDLE_COLUMN_TITLE = 'Social'
FOOTER_MIDDLE_MENU = (('IG','http://instagram.com'),)
# FOOTER_RIGHT_COLUMN_TITLE = 'Other'
# FOOTER_RIGHT_MENU = ()
COPYRIGHT = '&copy; 2020'


#################
# Pagination
#################
#PAGINATION_PREVIOUS = ''
#PAGINATION_NEXT = ''

#################
# Page specific
#################
ARCHIVES_HEAD_TITLE = 'Archives'
ARCHIVES_HEAD_DESCRIPTION = 'Archives'
ARCHIVES_SUBHEADER_IMAGE = False
ARCHIVES_SUBHEADER_TITLE = 'Archives'
ARCHIVES_SUBHEADER_SUBTITLE = 'Where the past resides'
ARCHIVES_CONTENT_TITLE = 'Content'

ARTICLE_SUBHEADER_BY = 'By'
ARTICLE_SUBHEADER_PUBLISHED = 'Published on'
ARTICLE_SUBHEADER_MODIFIED = 'Last modified'
ARTICLE_SUBHEADER_IN = 'Category:'
ARTICLE_RELATED_POSTS_TITLE = 'Related Posts'
COMMENT_TITLE = 'Comments'

AUTHOR_HEAD_TITLE = 'Author'
AUTHOR_HEAD_DESCRIPTION = 'Author'
AUTHOR_SUBHEADER_SUBTITLE = 'Author'
AUTHOR_CONTENT_TITLE = 'Articles by '

AUTHORS_HEAD_TITLE = 'Authors'
AUTHORS_HEAD_DESCRIPTION = 'Authors'
AUTHORS_SUBHEADER_TITLE = 'Authors'
AUTHORS_SUBHEADER_SUBTITLE = ''

CATEGORIES_HEAD_TITLE = 'Categories'
CATEGORIES_HEAD_DESCRIPTION = 'Categories'
CATEGORIES_SUBHEADER_TITLE = 'Categories'
CATEGORIES_SUBHEADER_SUBTITLE = ''

CATEGORY_HEAD_TITLE = 'Category'
CATEGORY_SUBHEADER_TITLE = 'Category'
CATEGORY_SUBHEADER_SUBTITLE = ''
CATEGORY_ARTICLES_TITLE = 'Articles'
CATEGORY_SUBCATEGORIES_TITLE = 'Subcategories'

SUBCATEGORY_HEAD_TITLE = 'Category'
SUBCATEGORY_SUBHEADER_TITLE = 'Category'
SUBCATEGORY_SUBHEADER_SUBTITLE = ''
SUBCATEGORY_ARTICLES_TITLE = 'Articles'
SUBCATEGORY_SUBCATEGORIES_TITLE = 'Subcategories'

INDEX_HEAD_TITLE = 'Home'
INDEX_SUBHEADER_TITLE = 'The Cali Garmo'
INDEX_SUBHEADER_SUBTITLE = ''
INDEX_CONTENT_TITLE = 'Articles'

PERIOD_ARCHIVES_HEAD_TITLE = 'Period Archives'
PERIOD_ARCHIVES_HEAD_DESCRIPTION = 'Period Archives'
PERIOD_ARCHIVES_SUBHEADER_TITLE = 'Period Archives'
PERIOD_ARCHIVES_SUBHEADER_SUBTITLE = ''
PERIOD_ARCHIVES_CONTENT_TITLE = 'Content'

SEARCH_HEAD_TITLE = 'Search'
SEARCH_SUBHEADER_TITLE = 'Search'
SEARCH_SUBHEADER_SUBTITLE = ''

TAG_HEAD_TITLE = 'Tag'
TAG_HEAD_DESCRIPTION = 'Tag'
TAG_SUBHEADER_TITLE = 'Tag'
TAG_SUBHEADER_SUBTITLE = ''
TAG_CONTENT_TITLE = 'Articles tagged with'

TAGS_HEAD_TITLE = 'Tags'
TAGS_HEAD_DESCRIPTION = 'Tags'
TAGS_SUBHEADER_TITLE = 'Tags'
TAGS_SUBHEADER_SUBTITLE = ''
TAGS_CONTENT_TITLE = 'Tag'
TAGS_CONTENT_LIST = ''


import sys
sys.path.append('.')
from pelicanconf_fr import SUBSITE_FR

I18N_SUBSITES = {
        'fr': SUBSITE_FR
        }
