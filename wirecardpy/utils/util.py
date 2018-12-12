import base64
import requests
from wirecardpy.utils import constants

TOKEN = {}


def headers():
    _headers = {
        'Authorization': 'Basic {}'.format(TOKEN['API_TOKEN'])
    }
    return _headers


def set_api_authorization(api_token, api_key, sandbox=False):
    global TOKEN
    TOKEN['API_TOKEN'] = base64.b64encode('{}:{}'.format(api_token, api_key))
    TOKEN['base_url'] = constants.BASE_URL_SANDBOX if sandbox else constants.BASE_URL_LIVE


def get_base_url():
    return TOKEN['base_url']


def request_get(url, data={}):
    return requests.get(url, json=data, headers=headers())


def request_post(url, data):
    return requests.post(url, json=data, headers=headers())
