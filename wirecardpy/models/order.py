from wirecardpy.utils import util
from wirecardpy.utils import constants_sandbox


class Order(object):
    """docstring for Order"""
    @staticmethod
    def create(ownId, items, customer):
        url = constants_sandbox.ORDER_URL if util.is_sandbox() else ''
        data = {
            'ownId': ownId,
            'items': items,
            'customer': customer
        }

        return util.request_post(url=url, data=data).json()
