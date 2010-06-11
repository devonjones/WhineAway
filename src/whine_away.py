#!/usr/bin/env python
import sys
from whine_away.imap import *
from optparse import OptionParser
from twisted.python import log, logfile
from twisted.internet import reactor
from twisted.cred import portal

def main():
	usage = "usage: %prog [options]\n\n"
	parser = option_parser(usage)
	(options, args) = parser.parse_args()
	
	port = 143
		
	log.startLogging(sys.stdout)
	p = portal.Portal(MailUserRealm())
	p.registerChecker(NoopCredentialsChecker())
	factory = IMAPFactory()
	factory.portal = p

	reactor.listenTCP(port, factory)
	reactor.run()

def option_parser(usage):
	parser = OptionParser(usage=usage)
	return parser

if __name__ == "__main__":
	main()
