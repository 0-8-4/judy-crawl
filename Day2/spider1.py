import urllib.request

url = 'https://www.baidu.com/img/bd_logo1.png'

request = urllib.request.Request(url)
resposn = urllib.request.urlopen(request)

googlelogo = resposn.read()

with open('google.png','wb') as f:
    f.write(googlelogo)
    f.close()