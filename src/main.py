import requests


response = requests.get('https://httpbin.org/ip')
# print('Your IP is {0}'.format(response.json()['origin']))
resp = format(response.json()['origin'])
print(resp)
