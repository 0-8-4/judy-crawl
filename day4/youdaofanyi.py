from urllib import request, parse

import random

ua_list = [
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'
]

def loadPage(url, word):
    userAgent = random.choice(ua_list)
    headers = {'User-Agent': userAgent}

    req = request.Request(url, headers=headers)

    data= {
        'i': word,
        'from':'AUTO',
        'to': 'AUTO',
        'martresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15616147260797',
        'sign': '2fcf94806d5b42374843bead371bf289',
        'ts': '1561614726079',
        'bv': 'e2a78ed30c66e16a857c5b6486a1d326',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }

    data = parse.urlencode(data).encode('utf-8')

    res = request.urlopen(req, data=data)

    html = res.read()

    content = html.decode('utf-8')
    #print(content)

    return content

import  json

def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    content = loadPage(url, word)
    jsondict = json.loads(content)
    #print(content)



    return jsondict['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    word = input('Input the word you needto translate')

    result = translate(word)
    print(result)