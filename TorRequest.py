import requesocks
import requests
session = requesocks.session()
session.proxies = {'http': 'socks5://127.0.0.1:9150', 'https': 'socks5://127.0.0.1:9150'}
print session.get("http://httpbin.org/ip").text
print requests.get("http://httpbin.org/ip").text
