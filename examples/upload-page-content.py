#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
ret = mwc.uploadPageContent(
	pageID = None,
	pageTitle = "TestPage123456789",
	pageContent = "The quick brown fox jumps over the lazy dog.",
	summary = "",
	bIsMinor = True,
	bDebug = False)

ret.dump()










