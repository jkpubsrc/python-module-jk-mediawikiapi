#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
n = 0

print("-" * 160)
for namespaceInfo in sorted(mwc.namespaces, key=lambda x: x.namespaceID):
	print("{}: {}".format(namespaceInfo.namespaceID, namespaceInfo.names))
	n += 1
print("-" * 160)

print()
print(n, "namespaces.")










