# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DbspiderSpider(scrapy.Spider):
    name = 'dbSpider'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/top250?start='
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        item = DoubanItem()
        movie =response.xpath("//div[@class='info']")

        for each in movie:
            item['title'] = each.xpath('./div/a/span[1]/text()').extract()[0]
            item['info'] = each.xpath('./div[2]/p[1]/text()').extract()[0]
            item['ratings'] = each.xpath('./div[2]/div[1]/span[2]/text()').extract()[0]
            item['review'] = each.xpath('./div[2]/p[2]/span/text()').extract()[0]



            #for key, value in item.item():
                #item[key] = item[value].replace(' ', '')


            yield item
        print('------------------------------------------------------------------------')

        if self.offset < 250:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
            #with open('douban.html', 'w', encoding='utf-8') as f:
            #f.write(str(response.body, encoding='utf-8'))
