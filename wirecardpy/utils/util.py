import base64
import requests
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
    else:
        status_code = response.status_code
        response_json = response.json()
        error_message = 'WIRECARD REQUEST ERROR: Status ' + str(status_code) + \
                        'Request not sent. May contain errors as missing required parameters or transcription error. '
        raise RequestException(error_message, response_json)


def set_api_authorization(api_token, api_key, sandbox=False):
    global TOKEN
    TOKEN['API_TOKEN'] = base64.b64encode('{}:{}'.format(api_token, api_key)).encode('utf-8')
    TOKEN['base_url'] = constants.BASE_URL_SANDBOX if sandbox else constants.BASE_URL_LIVE


def get_base_url():
    return TOKEN['base_url']


def request_get(url, data={}):
    return validate_response(requests.get(url, params=data, headers=headers()))


def request_post(url, data, access_token=None):
    if access_token:
        headers = oauth2_headers(access_token)
    else:
        headers = headers()
    return validate_response(requests.post(url, json=data, headers=headers))
