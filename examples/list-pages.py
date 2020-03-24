#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
n = 0
for pageInfo in mwc.listPages(bDebug = False):
	print()
	pageInfo.dump()
	n += 1
print()
print(n, "pages.")










