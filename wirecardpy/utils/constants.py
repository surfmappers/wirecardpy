from wirecardpy.utils.util import is_sandbox

# Define both API urls
BASE_URL_SANDBOX = 'https://sandbox.moip.com.br/v2/'
BASE_URL_LIVE = 'https://api.moip.com.br/v2/'

# Define which one will be used
BASE_URL = BASE_URL_SANDBOX if is_sandbox() else BASE_URL_LIVE

# Account constants
ACCOUNT_URL = BASE_URL + 'accounts/'
ACCOUNT_GET_URL = BASE_URL + ACCOUNT_URL + '/{0}'
ACCOUNT_EXISTS = BASE_URL + ACCOUNT_URL + '/exists'

# Order constants
ORDER_URL = BASE_URL + 'orders/'
ORDER_PAYMENT_URL = BASE_URL + ORDER_URL + '{0}/payments'
