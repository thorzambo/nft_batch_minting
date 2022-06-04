''' curl 'https://patient-billowing-moon.solana-mainnet.quiknode.pro/826c360201e137f0f078c807e8d8743a07831870/' \
  -H 'authority: patient-billowing-moon.solana-mainnet.quiknode.pro' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'origin: https://mint.ghostfacelabs.com' \
  -H 'referer: https://mint.ghostfacelabs.com/' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36' \
  --data-raw '{"method":"getAccountInfo","jsonrpc":"2.0","params":["FGjvRaVqC6FczVUXf1cpQfzNxRDYAWZuyfKvGfYvjYU",{"encoding":"base64"}],"id":"1f53ee5b-f891-430f-85f6-6135a0e5f18c"}' \
  --compressed '''
  
import requests

headers = {
    'authority': 'patient-billowing-moon.solana-mainnet.quiknode.pro',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://mint.ghostfacelabs.com',
    'referer': 'https://mint.ghostfacelabs.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
}

json_data = {
    'method': 'getAccountInfo',
    'jsonrpc': '2.0',
    'params': [
        'FGjvRaVqC6FczVUXf1cpQfzNxRDYAWZuyfKvGfYvjYU',
        {
            'encoding': 'base64',
        },
    ],
    'id': '1f53ee5b-f891-430f-85f6-6135a0e5f18c',
}

response = requests.post('https://patient-billowing-moon.solana-mainnet.quiknode.pro/826c360201e137f0f078c807e8d8743a07831870/', headers=headers, json=json_data)