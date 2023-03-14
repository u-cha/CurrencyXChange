routes = {

    '/currencies': {
        'method': {
            'get': 'get_currencies'
        }
    },
    '/currency': {
        'method': {
            'get': 'get_currency',
            'post': 'post_currency',
            }
    },

    '/exchangerates': {
        'method': {
            'get': 'get_exchange_rates'

        }
    },
    '/exchangerate': {
        'method': {
            'get': 'get_exchange_rate',
            'post': 'post_exchange_rate',
            'patch': 'patch_exchange_rate'
        }
    },
    '/exchange': {
        'method': {
            'get': 'exchange'
        }
    },
    '404': {
        'htmlpage': '404.html'
    }
}