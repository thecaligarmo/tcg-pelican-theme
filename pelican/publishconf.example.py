#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


DELETE_OUTPUT_DIRECTORY = True
SITEURL = 'http://thecaligarmo.com/dev/pelican' # Make sure it matche Makefile


MENUITEMS = (('Home', SITEURL),)

MENUITEMS_FR = (('Acceuil', 'http://thecaligarmo.com/dev/pelican/fr'),)

I18N_SUBSITES['fr']['MENUITEMS'] = MENUITEMS_FR
