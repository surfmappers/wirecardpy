from wirecardpy.utils import util
from wirecardpy.utils import constants


class Order(object):
    @staticmethod
    def create(ownId, items, customer):
        url = constants.ORDER_URL
        data = {
            'ownId': ownId,
            'items': items,
            'customer': customer
        }

        return util.request_post(url=url, data=data).json()
