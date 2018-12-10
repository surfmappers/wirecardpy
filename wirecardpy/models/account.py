from wirecardpy.utils import util
from wirecardpy.utils import constants


class Account(object):
    @staticmethod
    def exists(data):
        url = constants.ACCOUNT_EXISTS
        util.request_get(url, data)
