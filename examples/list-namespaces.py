#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
n = 0
for namespaceInfo in mwc.namespaces:
	print()
	namespaceInfo.dump()
	n += 1
print()
print(n, "namespaces.")










