import urllib
from urllib import request, parse

from lxml import etree
import ssl

#myself
import  time


def loadPage(url, tiebaName):
    req = request.Request(url)
    context = ssl._create_unverified_context()
    res = request.urlopen(req, context=context)

    html = res.read()
    content = etree.HTML(html)

    #match
    #link_list = content.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")
    tiebaLouzhu = content.xpath("//div[@class='threadlist_author pull_right']/span/span/a/text()")
    tiebaTitle = content.xpath("//div[@class='t_con cleafix']/div/div/div/a/text()")
    tiebaBlurb = content.xpath("//div[@class='t_con cleafix']/div/div/div/div[1]/text()")
    tiebaUser = content.xpath("//div[@class='t_con cleafix']/div/div/div/span[1]/a/text()")
    tiebeResponse = content.xpath("//div[@class='t_con cleafix']/div/span/text()")

    #for link in link_list:
        #fullurl = 'https://tieba.baidu.com' + link
        #print(fullurl)
        ##loadImage(fullurl)

        #print(link_list)
        #print(Louzhu)
    f = open('%s-tieba.txt'%tiebaName, 'a+', encoding='utf-8')
    print(tiebaBlurb)

    for Louzhu, title, blurb, user, numResponse in zip(tiebaLouzhu, tiebaTitle,tiebaBlurb, tiebaUser, tiebeResponse):
        print(Louzhu)
        print(title)
        print(user)
        f.write('\nLouzhu:' + Louzhu + '\ntitle: ' + title + '\nblurb: ' + blurb + '\nlatest feed: ' + user + '\t\t' + '\nHuifu: ' + numResponse + '\n\n')
    f.close()

def tiebaSpider(url, beginPage, endPage, tiebaName):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + '&pn=' + str(pn)
        print(fullurl)
        loadPage(fullurl, tiebaName)

if __name__ == '__main__':

    key = input('Input tieba name')
    kw = {'kw': key}
    parsem = parse.urlencode(kw)

    beginPage = int(input('input begin'))
    endPage = int(input('input end page'))
    url = 'http://tieba.baidu.com/f?' + parsem

    tiebaSpider(url, beginPage, endPage, key)


    #url = 'http://tieba.baidu.com/f?kw=%E5%9B%BE%E6%8B%89%E4%B8%81&ie=utf-8&pn=0'
    #loadPage(url)