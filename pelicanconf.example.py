#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


########################################
# Settings
########################################


PATH = 'content'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u'en'

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
PLUGINS = ['i18n_subsites', 'dateish', 'tipue_search']

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

#################
# Styling
#################
FONT_CSS = '<link href="https://fonts.googleapis.com/css?family=Amiri&display=swap" rel="stylesheet">'
FONT_FAMILY = "font-family: 'Amiri', serif;"
# CUSTOM_CSS = ''

#################
# Header
#################
HEADER_TITLE = 'The Cali Garmo'
HEADER_SUBTITLE = 'does Learning'
HEADER_IMAGE = False
HEADER_COLOR = '#356689'
HEADER_LOGO = False

HEADER_TITLE_FR = 'Le Cali Garmo'
HEADER_SUBTITLE_FR = 'en train d\'apprendre'


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
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_PAGINATION = False




########################################
# Text - Can alter for languages
########################################
AUTHOR = u'thecaligarmo'
SITENAME = u'The Cali Garmo is Learning'
SITE_DESCRIPTION = u'The Cali Garmo is Learning. Be it Maths, Languages, or Life Lessons.'
SITEURL = 'http://thecaligarmo.com/pelican/output'
THEME = 'theme/thecaligarmo'

#################
# Navigation
#################
MENUITEMS = (('Home', SITEURL),
             )

#################
# Footer
#################
FOOTER_LEFT_COLUMN_TITLE = 'The Cali Garmo'
FOOTER_LEFT_MENU = (('Home','http://thecaligarmo.com/'),)
FOOTER_MIDDLE_COLUMN_TITLE = 'Social'
FOOTER_MIDDLE_MENU = (('IG','ig.com'),)
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
