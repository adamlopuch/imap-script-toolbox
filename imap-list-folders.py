#!/usr/bin/env python
# encoding: utf-8
"""
Lists folders in IMAP mailbox.
"""
from __future__ import unicode_literals
import sys
import pandas as pd
from imapclient import IMAPClient
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

    source_account = IMAPClientObj(config.SOURCE_IMAP)

    print "CONNECTED: ", source_account
    print source_account.list_folders()
    #print "DEBUG: printing with length: %d" % (len(server.list_folders()))
    #print server.list_folders()


class IMAPClientObj(object):
    def __init__(self, conf):
        self.username = conf['USERNAME']
        self.host = conf['HOST']
        self.server = IMAPClient(conf['HOST'], use_uid=True, ssl=conf['SSL'])
        self.server.login(conf['USERNAME'], conf['PASSWORD'])

    def __str__(self):
        return "<user: %s | host: %s>" % (self.username, self.host)

    def folder_separator(self):
        return self.server.namespace()[0][0][1]

    def list_folders(self):
        return sorted(folderinfo[2] for folderinfo in self.server.list_folders())


if __name__ == '__main__':
    #TBD: stream writer stuff here

    parser = OptionParser()
    parser.add_option('-c', action="store", dest="config_filename", default="conf", help="Specifies IMAP configuration file to use. (OPTIONAL; defaults to: conf)")

    (options, args) = parser.parse_args()

    mainProgram(options)
