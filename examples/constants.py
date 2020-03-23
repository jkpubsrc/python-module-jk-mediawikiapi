#!/usr/bin/python3



import jk_json
import jk_pwdinput
import jk_json

from jk_mediawikiapi import *



cfg = jk_json.loadFromFile("constants.local.json")

URL = cfg["url"]
WIKI_USER_NAME = cfg["user"]
WIKI_PASSWORD = jk_pwdinput.readpwd("Password: ")











