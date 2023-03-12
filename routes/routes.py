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
        'htmlpage': 'exchangerate.html'
    },
    '/exchange': {
        'method': {
            'get': 'exchangerate'
        }
    },
    '404': {
        'htmlpage': '404.html'
    }
}