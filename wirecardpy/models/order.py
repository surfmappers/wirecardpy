from wirecardpy import util


class Order(object):
    """docstring for Order"""
    @staticmethod
    def create(ownId, items, customer):
        url = 'https://sandbox.moip.com.br/v2/orders'
        data = {
            'ownId': ownId,
            'items': items,
            'customer': customer
        }

        return util.request_post(url=url, data=data).json()
