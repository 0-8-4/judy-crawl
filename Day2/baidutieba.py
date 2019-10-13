from urllib import request, parse
import ssl

import random

UA_LIST = [
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'
]

def loadPage(url):
    user_agent = random.choice(UA_LIST)
    headers = {'User-Agent': user_agent}
    context = ssl._create_unverified_context()

    req = request.Request(url, headers = headers)
    res = request.urlopen(req, context = context)
    html = res.read()
    html = html.decode('utf-8')
    return html

def writePage(html,filename):
    with open(filename, 'w',encoding='utf-8') as f:
        f.write(html)
        f.close()
        print('done',filename)


def tiebaSpider(url, beginPage, endPage, tiebaName):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + '&pn=' + str(pn)

        print('Done', fullurl)

        html = loadPage(fullurl)
        writePage(html, '%s吧第%d页'%(tiebaName, page))

if __name__ == '__main__':
    key = input('Input url')
    kw = {'kw': key}
    parsem = parse.urlencode(kw)

    beginPage = int(input('input begin'))
    endPage = int(input('input end page'))

    url = 'http://tieba.baidu.com/f?' + parsem
    #'http://tieba.baidu.com/f?kw=%E5%9B%BE%E6%8B%89%E4%B8%81&ie=utf-8'
    tiebaSpider(url, beginPage, endPage, key)
    #html = loadPage(url)
    #writePage(html, 'firstpage.html')










