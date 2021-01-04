

import os


import jk_json
import jk_pwdinput
import jk_json

from jk_mediawikiapi import *


if os.path.isfile("constants.local.json"):
	cfg = jk_json.loadFromFile("constants.local.json")
elif os.path.isfile("constants.local.jsonc"):
	cfg = jk_json.loadFromFile("constants.local.jsonc")
else:
	raise Exception("Configuration file required: 'constants.local.json' or 'constants.local.jsonc'")

URL = cfg["url"]

WIKI_USER_NAME = cfg["user"]
if ("pwd" in cfg) and cfg["pwd"]:
	WIKI_PASSWORD = cfg["pwd"]
else:
	WIKI_PASSWORD = jk_pwdinput.readpwd("Password for wiki user " + repr(WIKI_USER_NAME) + ": ")

OTHER_USER = cfg["someOtherUser"]
if "someOtherUserPwd" in cfg:
	OTHER_USER_PASSWORD = cfg["someOtherUserPwd"]
else:
	OTHER_USER_PASSWORD = jk_pwdinput.readpwd("Password for wiki user " + repr(OTHER_USER) + ": ")










