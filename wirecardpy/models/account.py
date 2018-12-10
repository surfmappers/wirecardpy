from wirecardpy.utils import util
from wirecardpy.utils import constants


class Account(object):
    @staticmethod
    def exists(data):
        url = constants.ACCOUNT_EXISTS
        return util.request_get(url, data)

    @staticmethod
    def create(data):
        url = constants.ACCOUNT_URL
        return util.request_post(url, data)

    def get(account_id):
        url = constants.ACCOUNT_GET_URL.format(account_id)
        return util.request_get(url)
