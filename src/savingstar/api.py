# -*- coding: utf-8 -*-
#
import requests

errors = {-1: 'unexpected error',
           1: 'validation error',
           2: 'email_address not specified',
           3: 'password not specified',
           4: 'invalid email address password combination',
           5: 'both zip code and lat lon specified',
           6: 'lat specified without lon',
           7: 'lon specified without lat',
           8: 'zip code must be 5 digits long',
           9: 'invalid lat value',
           10: 'invalid lon value',
           11: 'invalid radius value',
           12: 'unknown user_id',
           13: 'unknown user_id_proxy',
           14: 'both user_id and user_id_proxy specified',
           15: 'neither user_id nor user_id_proxy specified',
           16: 'unknown tracking id',
           17: 'permission denied, not owner of tracking id',
           18: 'unknown namespace',
           19: 'duplicate tracking id',
           20: 'namespace not specified',
           21: 'value not specified',
           22: 'id not specified',
           23: 'unknown coupon id',
           24: 'coupon id not specified',
           25: 'coupon expired',
           26: 'coupon activation cap reached',
           27: 'coupon already activated by user',
           28: 'user must have at least one tracking id registered to activate coupon',
           29: 'retailer id not specified',
           30: 'unknown retailer id',
           31: 'coupon activated on the same card in another service',
           32: 'user_id_proxy not specified',
           33: 'duplicate user_id_proxy',
           34: 'email address is already associated with an account',
           37: 'the eCoupon could not be activated because it is not available at: Store 1, Store 2, ...',
           38: 'user_id not specified',
           50: 'payout_type not specified',
           51: 'invalid payout type',
           52: 'amount not specified',
           53: 'invalid amount',
           54: 'insufficient funds',
           55: 'paypal_email_address not specified',
           56: 'invalid paypal_email_address',
           57: 'bank_account_type not specified',
           58: 'invalid bank_account_type',
           59: 'bank_routing_number not specified',
           60: 'invalid bank_routing_number',
           61: 'bank_account_number not specified',
           62: 'invalid bank_account_number',
           63: 'email address not confirmed',
           64: 'tracking id already registered in another account',
           70: 'invalid product',
           80: 'fb_uid not specified',
           81: 'Unable to save the Facebook UID'
           }

class SavingStarAPI(object):

    def __init__(self, access_token=None, client_id=None, client_secret=None):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret

        # OAuth
        #
        if self.access_token is None:
            x = self._getOAuthToken()
            if 'access_token' in x.keys():
                self.access_token = x['access_token']

    def getAccessToken(self):
        return self.access_token
        
    def _getOAuthToken(self):
        url = "https://api.savingstar.com/oauth/access_token"
        payload = {'client_id': self.client_id,
                   'client_secret': self.client_secret,
                   'grant_type': 'none'
                   }
        return self._doPost(url, payload)

    def _doGet(self, url):
        headers = {"Authorization": "OAuth " + self.access_token,
                   "Accept": "application/vnd.savingstar; version=2"
                   }
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            try:
                return resp.json()
            except ValueError:
                return {'error': {'code': resp.status_code,
                                  'message': resp.text
                                  }
                                  }

    def _doPost(self, url, payload):
        if self.access_token is not None:
            headers = {"Authorization": "OAuth " + self.access_token,
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
                return {'error': {'code': resp.status_code,
                                  'message': resp.text
                                  }
                                  }

    def _doDelete(self, url, payload):
        if self.access_token is not None:
            headers = {"Authorization": "OAuth " + self.access_token,
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
                return {'error': {'code': resp.status_code,
                                  'message': resp.text
                                  }
                                  }

    # Coupon-related
    #
    def getAllCoupons(self):
        url = "https://api.savingstar.com/coupons.json"
        return self._doGet(url)

    def activateCoupon(self,
                       coupon_id,
                       user_id=None,
                       user_id_proxy=None,
                       channel=1):
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
        return self._doPost(url, payload)

    def externalCouponActivate(self,
                               external_coupon_id,
                               tracking_id_value,
                               retailer_id):
        url = "https://api.savingstar.com/coupons/external_activation.json"
        payload = {'external_coupon_id': external_coupon_id,
                   'tracking_id_value': tracking_id_value,
                   'retailer_id': retailer_id
                   }
        return self._doPost(url, payload)

    def getCouponStatuses(self):
        url = "https://api.savingstar.com/coupons/status.json"
        return self._doGet(url)

    def couponProductSearch(self, coupon_id, product):
        url = "https://api.savingstar.com/coupons/{0}/products.json?product={1}".format(coupon_id, product)
        return self._doGet(url)

    def getIncludedProducts(self, coupon_id):
        url = "https://api.savingstar.com/coupons/{0}/included_products.json".format(coupon_id)
        return self._doGet(url)

    # Retailer_Location-related
    #
    def getRetailerLocationsByZip(self, zipcode, radius=30):
        url = "https://api.savingstar.com/retailer_locations.json?zipcode={0}&radius={1}".format(zipcode, radius)
        return self._doGet(url)

    def getRetailerLocationsByLatLng(self, lat, lng, radius=30):
        url = "https://api.savingstar.com/retailer_locations.json?lat={0}&lon={1}&radius={2}".format(lat, lng, radius)
        return self._doGet(url)

    # Retailer-related
    #
    def getAllRetailers(self):
        url = "https://api.savingstar.com/retailers.json"
        return self._doGet(url)

    def getRetailer(self, retailer_id):
        url = "https://api.savingstar.com/{0}.json".format(retailer_id)
        return self._doGet(url)

    def retailerGeographicalSearch(self,
                                   lat=None,
                                   lng=None,
                                   zipcode=None,
                                   radius=10):
        if zipcode is None:
            url = "https://api.savingstar.com/retailers.json?lat={0}&lon={1}&radius={2}".format(lat, lng, radius)
        else:
            url = "https://api.savingstar.com/retailers.json?zipcode={0}&radius={1}".format(zipcode, radius)
        return self._doGet(url)

    def retailerSpecificLocationGeographicalSearch(self,
                                                   retailer_id,
                                                   lat=None,
                                                   lng=None,
                                                   zipcode=None,
                                                   radius=10):
        if zipcode is None:
            url = "https://api.savingstar.com/retailers/{0}/retailer_locations.json?lat={1}&lon={2}&radius={3}".format(retailer_id, lat, lng, radius)
        else:
            url = "https://api.savingstar.com/retailers/{0}/retailer_locations.json?zipcode={1}&radius={2}".format(retailer_id, zipcode, radius)
        return self._doGet(url)

    # Tracking_id-related
    #
    def getRegisteredTrackingIds(self, user_id=None, user_id_proxy=None):
        if user_id_proxy is None:
            url = "https://api.savingstar.com/tracking_ids.json?user_id={0}".format(user_id)
        else:
            url = "https://api.savingstar.com/tracking_ids.json?user_id_proxy={0}".format(user_id_proxy)
        return self._doGet(url)

    def getRegisteredTrackingId(self,
                                tracking_id,
                                user_id=None,
                                user_id_proxy=None):
        if user_id_proxy is None:
            url = "https://api.savingstar.com/{0}.json?user_id={1}".format(tracking_id, user_id)
        else:
            url = "https://api.savingstar.com/{0}.json?user_id_proxy={1}".format(tracking_id, user_id_proxy)
        return self._doGet(url)

    def registerTrackingId(self,
                           namespace,
                           retailer_id,
                           value,
                           user_id=None,
                           user_id_proxy=None):
        url = "https://api.savingstar.com/tracking_ids.json"
        if user_id_proxy is None:
            payload = {'user_id': user_id}
        else:
            payload = {'user_id_proxy': user_id_proxy}
        payload['namespace'] = namespace
        payload['retailer_id'] = retailer_id
        payload['value'] = value

        return self._doPost(url, payload)

    def removeTrackingId(self, id, user_id=None, user_id_proxy=None):
        url = "https://api.savingstar.com/tracking_ids.json"
        if user_id_proxy is None:
            payload = {'user_id': user_id}
        else:
            payload = {'user_id_proxy': user_id_proxy}
        payload['id'] = id

        return self._doDelete(url, payload)

    # User-related
    #
    def createUser(self, email_address, password):
        url = "https://api.savingstar.com/users.json"
        payload = {'email_address': email_address,
                   'password': password
                   }
        return self._doPost(url, payload)

    def authenticateUser(self, email_address, password):
        url = "https://api.savingstar.com/auth.json"
        payload = {'email_address': email_address,
                   'password': password
                   }
        return self._doPost(url, payload)

    def resetPassword(self, user_id):
        url = "https://api.savingstar.com/reset_password.json"
        payload = {'user_id': user_id}
        return self._doPost(url, payload)

    def createProxyUser(self, user_id_proxy):
        url = "https://api.savingstar.com/proxy.json"
        payload = {'user_id_proxy': user_id_proxy}
        return self._doPost(url, payload)

    def getAccountDetails(self, user_id=None, user_id_proxy=None):
        if user_id_proxy is None:
            url = "https://api.savingstar.com/account.json?user_id={0}".format(user_id)
        else:
            url = "https://api.savingstar.com/account.json?user_id_proxy={0}".format(user_id_proxy)
        return self._doGet(url)

    def getAccountHistory(self, user_id=None, user_id_proxy=None, lookback=90):
        if user_id_proxy is None:
            url = "https://api.savingstar.com/history.json?user_id={0}&lookback={1}".format(user_id, lookback)
        else:
            url = "https://api.savingstar.com/history.json?user_id_proxy={0}&lookback={1}".format(user_id_proxy, lookback)
        return self._doGet(url)

    def requestPayout(self,
                      payout_type,
                      amount,
                      user_id=None,
                      user_id_proxy=None,
                      paypal_email_address=None,
                      bank_account_type=None,
                      bank_account_number=None,
                      bank_routing_number=None):
        url = "https://api.savingstar.com/payout_request.json"
        if user_id_proxy is None:
            payload = {'user_id': user_id}
        else:
            payload = {'user_id_proxy': user_id_proxy}
        payload['payout_type'] = payout_type
        payload['amount'] = amount
        if payout_type == 'paypal':
            payload['paypal_email_address'] = paypal_email_address
        if payout_type == 'ach':
            payload['bank_account_type'] = bank_account_type
            payload['bank_account_number'] = bank_account_number
            payload['bank_routing_number'] = bank_routing_number

        return self._doPost(url, payload)
