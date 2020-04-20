#!/usr/bin/env python
# -*- coding :  utf-8 -*- #
########################################
# Text - Can alter for languages
########################################
# ensure it matches output in Makefile
SITEURL = "http://thecaligarmo.com/dev/pelican/fr"

SUBSITE_FR = {
    "SITEURL" : SITEURL,
    "THEME" : "theme/thecaligarmo",
    "AUTHOR" : "thecaligarmo",
    "MENUITEMS" : (("Acceuil", SITEURL),),
#################
# Footer
#################
    "FOOTER_LEFT_MENU" : (("Accueil","http://thecaligarmo.com/"),),
    "FOOTER_MIDDLE_MENU" : (("IG","http://instagram.com"),),
    # FOOTER_RIGHT_MENU : (),
    "COPYRIGHT" : "&copy; 2020",

#################
# Pagination
#################
    # "PAGINATION_PREVIOUS" : "",
    # "PAGINATION_NEXT" : "",

#################
# Site
#################
    "SITENAME" : "The Cali Garmo is Learning",
    "SITE_DESCRIPTION" : "The Cali Garmo is Learning. Be it Maths, Languages, or Life Lessons.",

#################
# Header
#################
    "HEADER_TITLE" : "The Cali Garmo",
    "HEADER_SUBTITLE" : "tests pelican",

#################
# Footer
#################
    "FOOTER_LEFT_COLUMN_TITLE" : "The Cali Garmo",
    "FOOTER_MIDDLE_COLUMN_TITLE" : "Social",
# FOOTER_RIGHT_COLUMN_TITLE = "Other",

#################
# Page specific
#################
    "ARCHIVES_HEAD_TITLE" : "Archives",
    "ARCHIVES_HEAD_DESCRIPTION" : "Archives",
    "ARCHIVES_SUBHEADER_TITLE" : "Archives",
    "ARCHIVES_SUBHEADER_SUBTITLE" : "Where the past resides",
    "ARCHIVES_CONTENT_TITLE" : "Content",

    "ARTICLE_SUBHEADER_BY" : "Par",
    "ARTICLE_SUBHEADER_PUBLISHED" : "Published on",
    "ARTICLE_SUBHEADER_MODIFIED" : "Last modified",
    "ARTICLE_SUBHEADER_IN" : "Catégorie : ",
    "ARTICLE_RELATED_POSTS_TITLE" : "Related Posts",
    "COMMENT_TITLE" : "Comments",

    "AUTHOR_HEAD_TITLE" : "Auteur",
    "AUTHOR_HEAD_DESCRIPTION" : "Auteur",
    "AUTHOR_SUBHEADER_SUBTITLE" : "Auteur",
    "AUTHOR_CONTENT_TITLE" : "Articles by ",

    "AUTHORS_HEAD_TITLE" : "Auteurs",
    "AUTHORS_HEAD_DESCRIPTION" : "Auteurs",
    "AUTHORS_SUBHEADER_TITLE" : "Auteurs",
    "AUTHORS_SUBHEADER_SUBTITLE" : "",

    "CATEGORIES_HEAD_TITLE" : "Catégories",
    "CATEGORIES_HEAD_DESCRIPTION" : "Catégories",
    "CATEGORIES_SUBHEADER_TITLE" : "Catégories",
    "CATEGORIES_SUBHEADER_SUBTITLE" : "",

    "CATEGORY_HEAD_TITLE" : "Catégorie",
    "CATEGORY_SUBHEADER_TITLE" : "Catégorie",
    "CATEGORY_SUBHEADER_SUBTITLE" : "",
    "CATEGORY_ARTICLES_TITLE" : "Articles",
    "CATEGORY_SUBCATEGORIES_TITLE" : "Subcatégories",

    "INDEX_HEAD_TITLE" : "Home",
    "INDEX_SUBHEADER_TITLE" : "The Cali Garmo",
    "INDEX_SUBHEADER_SUBTITLE" : "",
    "INDEX_CONTENT_TITLE" : "Articles",

    "PERIOD_ARCHIVES_HEAD_TITLE" : "Period Archives",
    "PERIOD_ARCHIVES_HEAD_DESCRIPTION" : "Period Archives",
    "PERIOD_ARCHIVES_SUBHEADER_TITLE" : "Period Archives",
    "PERIOD_ARCHIVES_SUBHEADER_SUBTITLE" : "",
    "PERIOD_ARCHIVES_CONTENT_TITLE" : "Content",

    "SEARCH_HEAD_TITLE" : "Search",
    "SEARCH_SUBHEADER_TITLE" : "Search",
    "SEARCH_SUBHEADER_SUBTITLE" : "",

    "TAG_HEAD_TITLE" : "Tag",
    "TAG_HEAD_DESCRIPTION" : "Tag",
    "TAG_SUBHEADER_TITLE" : "Tag",
    "TAG_SUBHEADER_SUBTITLE" : "",
    "TAG_CONTENT_TITLE" : "Articles tagged with",

    "TAGS_HEAD_TITLE" : "Tags",
    "TAGS_HEAD_DESCRIPTION" : "Tags",
    "TAGS_SUBHEADER_TITLE" : "Tags",
    "TAGS_SUBHEADER_SUBTITLE" : "",
    "TAGS_CONTENT_TITLE" : "Tag",
    "TAGS_CONTENT_LIST" : "",
}
