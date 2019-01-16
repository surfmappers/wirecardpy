from wirecardpy.utils import util
from wirecardpy.utils import constants


class Transfer(object):
    @staticmethod
    def create(access_token, data):
        url = util.get_base_url() + constants.TRANSFER_URL
        return util.request_post(url, data, access_token=access_token)
