# -*- coding: utf-8 -*-
import scrapy


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    def parse(self, response):
        pass
