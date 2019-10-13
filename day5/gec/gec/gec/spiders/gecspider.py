# -*- coding: utf-8 -*-
import scrapy
from gec.items import GecItem


#http://www.gec-edu.org


class GecspiderSpider(scrapy.Spider):
    name = 'gecspider'
    allowed_domains = ['gec-edu.org']
    start_urls = ['http://www.gec-edu.org/teachers/']




    def parse(self, response):
        item = GecItem()
        teacher = response.xpath("//div[@class='teacger-list']")

        for each in teacher:

            item['name'] = each.xpath("./div[@class='teacher-text']/h4/text()").extract()[0]
            item['title'] = each.xpath("./div[@class='teacher-text']/h6/text()").extract()[0]
            item['info'] = each.xpath("./div[@class='teacher-text']/p/text()").extract()[0]

            item['imglink'] = each.xpath("./div[@class='teacher-img']/img/@src").extract()[0]

            yield item



            print('done!-----------------------------------------------------------')
