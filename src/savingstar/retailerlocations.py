# -*- coding: utf-8 -*-
#
import common

def getRetailerLocationsByZip(access_token, zipcode, radius=30):
    url = "https://api.savingstar.com/retailer_locations.json?zipcode={0}&radius={1}".format(zipcode, radius)
    return common.doGet(access_token, url)

def getRetailerLocationsByLatLng(access_token, lat, lng, radius=30):
    url = "https://api.savingstar.com/retailer_locations.json?lat={0}&lon={1}&radius={2}".format(lat, lng, radius)
    return common.doGet(access_token, url)
