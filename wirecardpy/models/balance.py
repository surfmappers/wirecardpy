from wirecardpy.utils import util
from wirecardpy.utils import constants


class Balance(object):
    @staticmethod
    def get_balance(access_token):
        url = util.get_base_url() + constants.BALANCE_URL
        return util.request_get(url, access_token=access_token)
