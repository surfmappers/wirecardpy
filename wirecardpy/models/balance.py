from wirecardpy.utils import util
from wirecardpy.utils import constants


class Balance(object):
    @staticmethod
    def get_balance(access_token):
        return util.request_get(constants.BALANCE_URL, access_token=access_token)
