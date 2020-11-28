#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *





FILE_PATH = "water_droplets_on_leaf.pdf"

UPLOAD_FILE_NAME = "WaterDropletsOnLeaf.pdf"




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)

ret = mwc.uploadFile(FILE_PATH, UPLOAD_FILE_NAME, bDebug = False)

ret.dump()







