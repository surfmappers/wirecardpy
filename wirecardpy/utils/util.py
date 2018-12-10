import base64
import requests

TOKEN = {}


def headers():
    _headers = {
        'Authorization': 'Basic {}'.format(TOKEN['API_TOKEN'])
    }
    return _headers


def set_api_authorization(api_token, api_key, sandbox=False):
    global TOKEN
    TOKEN['API_TOKEN'] = base64.b64encode('{}:{}'.format(api_token, api_key))
    TOKEN['sandbox'] = sandbox


def is_sandbox():
    return TOKEN['sandbox'] if 'sandbox' in TOKEN else False


def request_get(url, data={}):
    return requests.get(url, json=data, headers=headers())


def request_post(url, data):
    return requests.post(url, json=data, headers=headers())
