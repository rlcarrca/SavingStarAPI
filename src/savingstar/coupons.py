# -*- coding: utf-8 -*-
#
import common

def getAllCoupons(access_token):
    url = "https://api.savingstar.com/coupons.json"
    return common.doGet(access_token, url)

def activateCoupon(access_token, coupon_id, user_id=None, user_id_proxy=None, channel=1):
    '''Note:
            for channel:
                1 - web
                2 - iPhone
                3 - android
    '''
    url = "https://api.savingstar.com/coupons.json"
    payload = {'id': coupon_id,
               'user_id': user_id,
               'channel': channel
               }
    return common.doPost(url, payload, access_token)

def externalCouponActivate(access_token, external_coupon_id, tracking_id_value, retailer_id):
    url = "https://api.savingstar.com/coupons/external_activation.json"
    payload = {'external_coupon_id': external_coupon_id,
               'tracking_id_value': tracking_id_value,
               'retailer_id': retailer_id
               }
    return common.doPost(url, payload, access_token)

def getCouponStatuses(access_token):
    url = "https://api.savingstar.com/coupons/status.json"
    return common.doGet(access_token, url)

def couponProductSearch(access_token, coupon_id, product):
    url = "https://api.savingstar.com/coupons/{0}/products.json?product={1}".format(coupon_id, product)
    return common.doGet(access_token, url)

def getIncludedProducts(access_token, coupon_id):
    url = "https://api.savingstar.com/coupons/{0}/included_products.json".format(coupon_id)
    return common.doGet(access_token, url)
