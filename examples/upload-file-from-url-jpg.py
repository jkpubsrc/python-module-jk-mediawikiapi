#!/usr/bin/python3



import jk_json
import jk_pwdinput

from constants import *

from jk_mediawikiapi import *





FILE_URL = "https://free-images.com/lg/6246/water_droplets_on_leaf.jpg"
UPLOAD_FILE_NAME = "WaterDropletsOnLeaf.jpg"




mwc = MediaWikiClient(URL, WIKI_USER_NAME, WIKI_PASSWORD)

ret = mwc.uploadFileFromURL(FILE_URL, UPLOAD_FILE_NAME, bDebug = False)

ret.dump()







