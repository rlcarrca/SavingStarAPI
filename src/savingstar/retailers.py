# -*- coding: utf-8 -*-
#
import common

def getAllRetailers(access_token):
    url = "https://api.savingstar.com/retailers.json"
    return common.doGet(access_token, url)

def getRetailer(access_token, retailer_id):
    url = "https://api.savingstar.com/{0}.json".format(retailer_id)
    return common.doGet(access_token, url)

def retailerGeographicalSearch(access_token, lat=None, lng=None, zipcode=None, radius=10):
    if zipcode is None:
        url = "https://api.savingstar.com/retailers.json?lat={0}&lon={1}&radius={2}".format(lat, lng, radius)
    else:
        url = "https://api.savingstar.com/retailers.json?zipcode={0}&radius={1}".format(zipcode, radius)
    return common.doGet(access_token, url)

def retailerSpecificLocationGeographicalSearch(access_token, retailer_id, lat=None, lng=None, zipcode=None, radius=10):
    if zipcode is None:
        url = "https://api.savingstar.com/retailers/{0}/retailer_locations.json?lat={1}&lon={2}&radius={3}".format(retailer_id, lat, lng, radius)
    else:
        url = "https://api.savingstar.com/retailers/{0}/retailer_locations.json?zipcode={1}&radius={2}".format(retailer_id, zipcode, radius)
    return common.doGet(access_token, url)
