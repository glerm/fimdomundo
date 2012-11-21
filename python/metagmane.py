# -*- coding: utf-8 -*-

import feedparser

metaRSS = feedparser.parse('http://rss.gmane.org/messages/complete/gmane.politics.organizations.metareciclagem')

teste=metaRSS.entries[13].summary

print teste

