# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request, parse

from lxml import etree
import ssl

class GecPipeline(object):
    imglink = ''

    def writeImage(self, link, filename):
        header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

        req = request.Request(link, headers=header)
        context = ssl._create_unverified_context()
        res = request.urlopen(req, context=context)

        image = res.read()
        immagename = 'image/%s.png'%filename
        with open(immagename, 'wb') as f:
            f.write(image)
            f.close()

    def process_item(self, item, spider):

        imgname = item['name']

        link = str(item['imglink'])
        fullurl = 'http://www.gec-edu.org' + link
        print(type(item['name']))
        print(fullurl)
        print(imgname)
        print(item['imglink'])
        print(type(item))


        with open('gec.txt', 'a+', encoding='utf-8') as f:
            f.write('\n\nName: ' + item['name'] + '\t\ttitle:' + item['title'] + '\t\tinfo:' + item['info'] + '\n\n')
            f.write('-----------------------------------------------------------------')


            self.writeImage(fullurl, imgname)
            f.close()
        return item
