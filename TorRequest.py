#!/usr/bin/env python

import requesocks

session = requesocks.session()
session.proxies = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}

print session.get("https://wtfismyip.com/text").text
