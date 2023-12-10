

import sys
import os
import typing

import jk_typing
#import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj
import jk_mediawikiapi
import jk_pwdinput



jData = jk_json.loadFromFile("test.jsonc")
URL = jData["url"]
LOGIN = jData["login"]
PWD = jk_pwdinput.readpwd("pwd:")



with jk_logging.wrapMain() as log:
	if os.name == 'nt':
		os.system("color")

	mediaWikiClient = jk_mediawikiapi.MediaWikiClient(URL, LOGIN, PWD, bDisableSSLCertCheck=True, bDebug=True)
	for c in mediaWikiClient.listCategories():
		print("-- ", c.name)




