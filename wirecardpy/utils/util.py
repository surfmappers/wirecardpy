import base64
import requests
from wirecardpy.utils import constants

TOKEN = {}


class RequestException(Exception):
    pass


def headers():
    _headers = {
        'Authorization': 'Basic {}'.format(TOKEN['API_TOKEN'])
    }
    return _headers


def validate_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        response_json = response.json()
        response_json['status_code'] = response.status_code
        raise RequestException(response_json)


def set_api_authorization(api_token, api_key, sandbox=False):
    global TOKEN
    TOKEN['API_TOKEN'] = base64.b64encode('{}:{}'.format(api_token, api_key))
    TOKEN['base_url'] = constants.BASE_URL_SANDBOX if sandbox else constants.BASE_URL_LIVE


def get_base_url():
    return TOKEN['base_url']


def request_get(url, data={}):
    return validate_response(requests.get(url, params=data, headers=headers()))


def request_post(url, data):
    return validate_response(requests.post(url, json=data, headers=headers()))
