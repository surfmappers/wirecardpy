import base64
import requests
import sys
from wirecardpy.utils import constants

TOKEN = {}


class RequestException(Exception):
    def __init__(self, msg, errors):
        Exception.__init__(self, msg)
        self.request_errors = errors


def headers():
    _headers = {
        'Authorization': 'Basic {}'.format(TOKEN['API_TOKEN'])
    }
    return _headers


def oauth2_headers(access_token):
    _headers = {
        'Authorization': 'Bearer ' + access_token,
    }
    return _headers


def validate_response(response):
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    elif response.status_code != 204:
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response_json = {'errors': [{'description': 'WIRECARD RETURN ERROR: ' + e.message}]}

        error_message = 'WIRECARD REQUEST ERROR: Status ' + str(status_code) + ' ' + \
                        'Request not sent. May contain errors as missing required parameters or transcription error. '
        raise RequestException(error_message, response_json)


def set_api_authorization(api_token, api_key, sandbox=False):
    global TOKEN
    to_encode = '{}:{}'.format(api_token, api_key)
    if sys.version_info >= (3, 0):
        to_encode = to_encode.encode('utf-8')
        TOKEN['API_TOKEN'] = base64.b64encode(to_encode).decode('utf-8')
    else:
        TOKEN['API_TOKEN'] = base64.b64encode(to_encode).encode('utf-8')
    TOKEN['base_url'] = constants.BASE_URL_SANDBOX if sandbox else constants.BASE_URL_LIVE


def get_base_url():
    return TOKEN['base_url']


def request_get(url, data={}, access_token=None):
    if access_token:
        auth_headers = oauth2_headers(access_token)
    else:
        auth_headers = headers()
    return validate_response(requests.get(url, params=data, headers=auth_headers))


def request_post(url, data, access_token=None):
    if access_token:
        auth_headers = oauth2_headers(access_token)
    else:
        auth_headers = headers()
    return validate_response(requests.post(url, json=data, headers=auth_headers))


def request_put(url, data, access_token):
    auth_headers = oauth2_headers(access_token)
    return validate_response(requests.put(url, json=data, headers=auth_headers))


def request_delete(url, access_token):
    auth_headers = oauth2_headers(access_token)
    return validate_response(requests.delete(url, headers=auth_headers))
