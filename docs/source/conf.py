# -*- coding: utf-8 -*-
import sys

sys.path.append('../../')

from shared_conf.conf import *

project = u'Open edX Learner\'s Guide'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Open_edX')
product = 'Open_edX'
set_audience(OPENEDX, LEARNERS)
html_static_path = ['_static']
the_builder = 'html'
def setup(app):
    app.add_js_file('.tx.js')
    app.add_config_value('product', '', True)
