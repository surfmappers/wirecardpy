from wirecardpy.utils import util
from wirecardpy.utils import constants


class BankAccount(object):
    @staticmethod
    def create(access_token, account_id, data):
        url = util.get_base_url() + constants.BANK_ACCOUNT_CREATE.format(account_id)
        return util.request_post(url, data, access_token=access_token)

    @staticmethod
    def update(access_token, bank_account_id, data):
        url = util.get_base_url() + constants.BANK_ACCOUNT_ID.format(bank_account_id)
        return util.request_put(url, data, access_token)
