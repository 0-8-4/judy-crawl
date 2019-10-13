import urllib.request

url = 'https://dig.chouti.com/'

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

req = urllib.request.Request(url, headers=header)

res = urllib.request.urlopen(req)

data = res.read().decode('utf-8')

with open('chouti.html','w',encoding='utf-8') as f:
    f.write(data)
    f.close()

