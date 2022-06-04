import requests
''' 

curl 'https://patient-billowing-moon.solana-mainnet.quiknode.pro/826c360201e137f0f078c807e8d8743a07831870/' \
  -X 'OPTIONS' \
  -H 'authority: patient-billowing-moon.solana-mainnet.quiknode.pro' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'access-control-request-headers: content-type' \
  -H 'access-control-request-method: POST' \
  -H 'origin: https://mint.ghostfacelabs.com' \
  -H 'referer: https://mint.ghostfacelabs.com/' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36' \
  --compressed '''

headers = {
    'authority': 'patient-billowing-moon.solana-mainnet.quiknode.pro',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-request-headers': 'content-type',
    'access-control-request-method': 'POST',
    'origin': 'https://mint.ghostfacelabs.com',
    'referer': 'https://mint.ghostfacelabs.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
}

response = requests.options('https://patient-billowing-moon.solana-mainnet.quiknode.pro/826c360201e137f0f078c807e8d8743a07831870/', headers=headers)
