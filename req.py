import requests
headers = {
	'Host':'github.com',
	'Connection':'close',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G800M Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'es-US,es-419;q=0.9,es;q=0.8'
}
req = requests.get('http://github.com/', headers=headers)
print req.text
