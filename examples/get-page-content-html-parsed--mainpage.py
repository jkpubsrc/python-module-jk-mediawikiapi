#!/usr/bin/python3



import bs4

import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)
parsedPage = mwc.getPageContentHTMLParsed(mwc.siteInfoMainPage, bDebug = False)
print(parsedPage.prettify())










