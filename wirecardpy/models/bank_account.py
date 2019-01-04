from wirecardpy.utils import util
from wirecardpy.utils import constants


class BankAccount(object):
    @staticmethod
    def create(access_token, account_id, data):
        url = constants.BANK_ACCOUNT_CREATE.format(account_id)
        util.request_post(url, data, access_token=access_token)
