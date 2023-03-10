routes = {
    '/': {
        'htmlpage': 'description.html'
    },
    '/currencies': {
        'method': 'get_currencies'
    },
    '/currency/': {
        'method': 'get_currency'
    },

    '/exchangerates': {
        'htmlpage': 'exchangerates.html'
    },
    '/exchangerate': {
        'htmlpage': 'exchangerate.html'
    },
    '/exchange': {
        'htmlpage': 'exchange.html'
    },
    '404': {
        'htmlpage': '404.html'
    }
}