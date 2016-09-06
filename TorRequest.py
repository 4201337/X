#!/usr/bin/env python

import requesocks

with requesocks.session() as req:
    
    req.proxies = {
        'http': 'socks5://127.0.0.1:9150',
        'https': 'socks5://127.0.0.1:9150'
    }
    
    req.headers = {
        'Accept': 'No',
        'Accept-Encoding': 'No',
        'Referer': 'http://1.3.3.7/',
        'User-Agent': '1337',
    }
    
    req.cert = ''
    
    req.stream = True
    
    try:
        url = req.get('https://httpbin.org/ip')
        print url.text
        url = req.get('https://httpbin.org/headers')
        print url.text
    except requesocks.exceptions.RequestException, e:
        print e
