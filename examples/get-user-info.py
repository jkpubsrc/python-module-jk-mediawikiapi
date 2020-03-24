#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
userInfo = mwc.getUserInfo(OTHER_USER, bDebug=False)
userInfo.dump()








