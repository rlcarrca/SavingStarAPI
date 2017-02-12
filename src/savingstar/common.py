# -*- coding: utf-8 -*-
#
import requests

def getOAuthToken(client_id, client_secret):
    url = "https://api.savingstar.com/oauth/access_token"
    payload = {'client_id': client_id,
               'client_secret': client_secret,
               'grant_type': 'none'
               }
    return doPost(url, payload)

def doGet(access_token, url):
    headers = {"Authorization": "OAuth " + access_token,
               "Accept": "application/vnd.savingstar; version=2"
               }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        try:
            return resp.json()
        except ValueError:
            return {'error': {'code': resp.status_code, 'message': resp.text}}

def doPost(url, payload, access_token=None):
    if access_token is not None:
        headers = {"Authorization": "OAuth " + access_token,
                   "Accept": "application/vnd.savingstar; version=2",
                   "Content-Type": "application/x-www-form-urlencoded"
                   }
        resp = requests.post(url, headers=headers, data=payload)
    else:
        resp = requests.post(url, data=payload)
    if resp.status_code == 200:
        return resp.json()
    else:
        try:
            return resp.json()
        except ValueError:
            return {'error': {'code': resp.status_code, 'message': resp.text}}

def doDelete(url, payload, access_token=None):
    if access_token is not None:
        headers = {"Authorization": "OAuth " + access_token,
                   "Accept": "application/vnd.savingstar; version=2",
                   "Content-Type": "application/x-www-form-urlencoded"
                   }
        resp = requests.delete(url, headers=headers, data=payload)
    else:
        resp = requests.delete(url, data=payload)
    if resp.status_code == 200:
        return resp.json()
    else:
        try:
            return resp.json()
        except ValueError:
            return {'error': {'code': resp.status_code, 'message': resp.text}}
