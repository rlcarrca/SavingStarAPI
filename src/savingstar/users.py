# -*- coding: utf-8 -*-
#
import common

def createUser(access_token, email_address, password):
    url = "https://api.savingstar.com/users.json"
    payload = {'email_address': email_address,
               'password': password
               }
    return common.doPost(url, payload, access_token)

def authenticateUser(access_token, email_address, password):
    url = "https://api.savingstar.com/auth.json"
    payload = {'email_address': email_address,
               'password': password
               }
    return common.doPost(url, payload, access_token)

def resetPassword(access_token, user_id):
    url = "https://api.savingstar.com/reset_password.json"
    payload = {'user_id': user_id
               }
    return common.doPost(url, payload, access_token)

def createProxyUser(access_token, user_id_proxy):
    url = "https://api.savingstar.com/proxy.json"
    payload = {'user_id_proxy': user_id_proxy
               }
    return common.doPost(url, payload, access_token)

def getAccountDetails(access_token, user_id=None, user_id_proxy=None):
    if user_id_proxy == None:
        url = "https://api.savingstar.com/account.json?user_id={0}".format(user_id)
    else:
        url = "https://api.savingstar.com/account.json?user_id_proxy={0}".format(user_id_proxy)
    return common.doGet(access_token, url)

def getAccountHistory(access_token, user_id=None, user_id_proxy=None, lookback=90):
    if user_id_proxy == None:
        url = "https://api.savingstar.com/history.json?user_id={0}&lookback={1}".format(user_id, lookback)
    else:
        url = "https://api.savingstar.com/history.json?user_id_proxy={0}&lookback={1}".format(user_id_proxy, lookback)
    return common.doGet(access_token, url)

def requestPayout(access_token, payout_type, amount, user_id=None,
                  user_id_proxy=None, paypal_email_address=None, bank_account_type=None,
                  bank_account_number=None, bank_routing_number=None):
    url = "https://api.savingstar.com/payout_request.json"
    if user_id_proxy == None:
        payload = {'user_id': user_id }
    else:
        payload = {'user_id_proxy': user_id_proxy }
    payload['payout_type'] = payout_type
    payload['amount'] = amount
    if payout_type == 'paypal':
        payload['paypal_email_address'] = paypal_email_address
    if payout_type == 'ach':
        payload['bank_account_type'] = bank_account_type
        payload['bank_account_number'] = bank_account_number
        payload['bank_routing_number'] = bank_routing_number

    return common.doPost(url, payload, access_token)
