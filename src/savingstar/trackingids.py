# -*- coding: utf-8 -*-
#
import common

def getRegisteredTrackingIds(access_token, user_id=None, user_id_proxy=None):
    if user_id_proxy == None:
        url = "https://api.savingstar.com/tracking_ids.json?user_id={0}".format(user_id)
    else:
        url = "https://api.savingstar.com/tracking_ids.json?user_id_proxy={0}".format(user_id_proxy)
    return common.doGet(access_token, url)

def getRegisteredTrackingId(access_token, tracking_id, user_id=None, user_id_proxy=None):
    if user_id_proxy == None:
        url = "https://api.savingstar.com/{0}.json?user_id={1}".format(tracking_id, user_id)
    else:
        url = "https://api.savingstar.com/{0}.json?user_id_proxy={1}".format(tracking_id, user_id_proxy)
    return common.doGet(access_token, url)

def registerTrackingId(access_token, namespace, retailer_id, value, user_id=None, user_id_proxy=None):
    url = "https://api.savingstar.com/tracking_ids.json"
    if user_id_proxy == None:
        payload = {'user_id': user_id }
    else:
        payload = {'user_id_proxy': user_id_proxy }
    payload['namespace'] = namespace
    payload['retailer_id'] = retailer_id
    payload['value'] = value

    return common.doPost(url, payload, access_token)

def removeTrackingId(access_token, id, user_id=None, user_id_proxy=None):
    url = "https://api.savingstar.com/tracking_ids.json"
    if user_id_proxy == None:
        payload = {'user_id': user_id }
    else:
        payload = {'user_id_proxy': user_id_proxy }
    payload['id'] = id

    return common.doDelete(url, payload, access_token)
