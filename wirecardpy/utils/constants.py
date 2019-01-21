# Define both API urls
BASE_URL_SANDBOX = 'https://sandbox.moip.com.br/v2/'
BASE_URL_LIVE = 'https://api.moip.com.br/v2/'

# Account constants
ACCOUNT_URL = 'accounts/'
ACCOUNT_GET_URL = ACCOUNT_URL + '{0}'
ACCOUNT_EXISTS = ACCOUNT_URL + 'exists'

# Order constants
ORDER_URL = 'orders/'
ORDER_PAYMENT_URL = ORDER_URL + '{0}/payments'

# Bank Account constants
BANK_ACCOUNT_CREATE = 'accounts/{0}/bankaccounts'
BANK_ACCOUNT_ID = 'bankaccounts/{0}'

# Balance
BALANCE_URL = 'balances'

# Transfer
TRANSFER_URL = 'transfers'
ANTICIPATION_ESTIMATIVE_URL = 'anticipationestimates?amount={0}'

# Notification
NOTIFICATION_URL = 'preferences/notifications'
REMOVE_NOTIFICATION_URL = NOTIFICATION_URL + '/{}'
