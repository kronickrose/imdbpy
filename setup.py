#!/usr/bin/env python

import sys
from distutils.core import setup, Extension

# --- CONFIGURE

# XXX NOTE: if you _really_ don't want to install the "local access
# system", set DO_LOCAL to 0.
# The local access system requires a C module and, to be used, the _whole_
# IMDb's database installed in your computer; this not useful/possible
# in small devices like handheld computers, where it makes sense to
# also save the little space taken by the local interface package or
# where you don't have the development environment needed to compile
# the C module.
# When possible it's _always safer_ to leave it to 1 (compile the C
# module and install the local interface) even without the whole
# IMDb's database installed; obviously it can't be used, but the
# interface to the web database is always available.
DO_LOCAL = 1
# Install some very simple example scripts.
DO_SCRIPTS = 1


# --- NOTHING TO CONFIGURE BELOW.

# version of the software; CVS releases contain a string
# like "-cvsYearMonthDay-OptionalChar".
version = '1.8-cvs050301'

home_page = 'http://imdbpy.sourceforge.net/'

long_desc = """IMDbPY is a Python package useful to retrieve and
manage the data of the IMDb movie database about both movies and people.

Platform-independent and written in pure Python (and few C lines),
it can retrieve data from both the IMDb's web server and a local copy
of the whole database.

IMDbPY package can be very easily used by programmers and developers
to provide access to the IMDb's data to their programs.

Some simple example scripts - useful for the end users - are included
in this package; other IMDbPY-based programs are available at the
home page: %s
""" % home_page

dwnl_url = 'http://imdbpy.sourceforge.net/?page=download'

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: Web Environment
Intended Audience :: Developers
Intended Audience :: End Users/Desktop
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Programming Language :: Python
Operating System :: OS Independent
Topic :: Database :: Front-Ends
Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries
Topic :: Software Development :: Libraries :: Python Modules
"""

ratober = Extension('imdb.parser.local.ratober',
                    ['imdb/parser/local/ratober.c'])

params = {'name': 'IMDbPY',
      'version': version,
      'description': 'Python package to access the IMDb\'s database',
      'long_description': long_desc,
      'author': 'Davide Alberani',
      'author_email': 'da@erlug.linux.it',
      'maintainer': 'Davide Alberani',
      'maintainer_email': 'da@erlug.linux.it',
      'url': home_page,
      'license': 'GPL',
      'packages': ['imdb', 'imdb.parser', 'imdb.parser.http']}

if DO_LOCAL:
    params['packages'] = params['packages'] + ['imdb.parser.local']
    params['ext_modules'] = [ratober]

if DO_SCRIPTS:
    params['scripts'] = ['./bin/get_first_movie', './bin/get_movie',
                        './bin/search_movie', './bin/get_first_person',
                        './bin/get_person', './bin/search_person']


if not hasattr(sys, 'version_info'):
    sys.version_info = (1, 5)

if sys.version_info >= (2, 1):
    params['keywords'] = ['imdb', 'movie', 'people', 'database', 'cinema',
                            'film', 'person', 'cast', 'actor', 'actress',
                            'director']
    params['platforms'] = 'any'

if sys.version_info >= (2, 3):
    params['download_url'] = dwnl_url
    params['classifiers'] = filter(None, classifiers.split("\n"))


if sys.version_info < (2, 0):
    apply(setup, [], params)
else:
    setup(**params)

