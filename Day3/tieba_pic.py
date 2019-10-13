import urllib
from urllib import request, parse

from lxml import etree
import ssl

#myself
import  time


def loadPage(url):
    req = request.Request(url)
    context = ssl._create_unverified_context()
    res = request.urlopen(req, context=context)

    html = res.read()
    content = etree.HTML(html)

    #match
    link_list = content.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")

    for link in link_list:
        fullurl = 'https://tieba.baidu.com' + link
        #print(fullurl)
        loadImage(fullurl)

        #print(link_list)

def loadImage(link):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

    req = request.Request(link, headers=header)

    context = ssl._create_unverified_context()

    res = request.urlopen(req, context=context)
    html = res.read()

    content = etree.HTML(html)

    link_list = content.xpath("//img[@class='BDE_Image']/@src")

    for link in link_list:
        print(link)
        #time.sleep(3)
        writeImage(link)

def writeImage(link):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

    req = request.Request(link, headers=header)

    context = ssl._create_unverified_context()

    res = request.urlopen(req, context=context)

    image = res.read()

    filename = link[-10:]

    with open('image/%s'%filename, 'wb') as f:
        f.write(image)
        f.close()

    print('Done', filename)
    url = 'http://tieba.baidu.com/f?' + parsem
def tiebaSpider(url, beginPage, endPage, tiebaName):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + '&pn=' + str(pn)

        loadPage(fullurl)

if __name__ == '__main__':
    #url = 'http://tieba.baidu.com/f?kw=%E5%9B%BE%E6%8B%89%E4%B8%81&ie=utf-8&pn=0'

    key = input('Input url')
    kw = {'kw': key}
    parsem = parse.urlencode(kw)

    beginPage = int(input('input begin'))
    endPage = int(input('input end page'))
    url = 'http://tieba.baidu.com/f?' + parsem

    tiebaSpider(url, beginPage, endPage, key)



    #loadPage(url)