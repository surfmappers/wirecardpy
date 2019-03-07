from wirecardpy.utils import util
from wirecardpy.utils import constants


class Order(object):
    @staticmethod
    def create(data):
        url = util.get_base_url() + constants.ORDER_URL
        return util.request_post(url=url, data=data)
