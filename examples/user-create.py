#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
if mwc.validatePassword(OTHER_USER, OTHER_USER_PASSWORD, bDebug=True):
	userInfo = mwc.createUser(OTHER_USER, OTHER_USER_PASSWORD, bDebug=True)
	userInfo.dump()
else:
	print("Password rejected!")








