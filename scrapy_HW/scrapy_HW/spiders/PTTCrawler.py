# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/M.1581055710.A.38E.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies={'over18': '1'})

    def parse(self, response):

        print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_item = soup.find('title')
        title = title_item.text if title_item else 'no title'
        print(f'title: {title}')

        pass
