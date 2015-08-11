#!/usr/bin/env python
# encoding: utf-8
"""
Template script framework for imap-script-toolbox
"""

import sys
from optparse import OptionParser

def mainProgram(options):
    # get the config file's namespace into an an object
    print "Using configuration file: %s.py" % (options.config_filename)
    try:
        config = __import__(options.config_filename)    # assumes <CONFIG_FILENAME>.py exists
    except:
        print "\nERROR: script exiting\n"
        print "Unable to import configuration file: %s.py" % (options.config_filename)
        print " * does this file exist?"
        print " * if passed manually, did you remember to remove .py from what you passed in?"
        sys.exit(1)

    # ROADMAP:
    # - open IMAP connection
    # - read in folders
    # - output folders to stdout

    print "DEBUG: config.SOURCE_IMAP=", config.SOURCE_IMAP

if __name__ == '__main__':
    #TBD: stream writer stuff here

    parser = OptionParser()
    parser.add_option('-c', action="store", dest="config_filename", default="conf", help="Specifies IMAP configuration file to use. (OPTIONAL; defaults to: conf)")

    (options, args) = parser.parse_args()

    mainProgram(options)
