# -*- coding: utf-8 -*-
import scrapy
from scrapy_HW.items import ScrapyHwItem


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler2'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/M.1581055710.A.38E.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies={'over18': '1'})

    def parse(self, response):

        # print(response.text)
        title = response.xpath('//title/text()').get()
        # print(f'title: {title}')

        item = ScrapyHwItem()
        item['title'] = title

        yield item
