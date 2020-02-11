# -*- coding: utf-8 -*-
import scrapy
from scrapy_HW.items import ScrapyHwItem
from bs4 import BeautifulSoup


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler2'
    allowed_domains = ['www.ptt.cc']
    # start_urls = ['https://www.ptt.cc/bbs/Gossiping/M.1581055710.A.38E.html']

    def __init__(self, board='NBA'):
        self.start_urls = [f'https://www.ptt.cc/bbs/{board}']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies={'over18': '1'})

    def parse(self, response):

        post_list = response.xpath('//div[@class="r-list-container action-bar-margin bbs-screen"]//div[@class="r-ent"]')

        for post in post_list:
            post_soup = BeautifulSoup(post.get(), 'html.parser')
            post_date = post_soup.find('div', class_='date')
            if post_date and post_date.text.strip() == '2/11':
                url_tag = post_soup.find('div', class_='title').find('a')
                url = url_tag.get('href')if url_tag else ''
                # print(url)

                yield scrapy.Request(url=f'https://www.ptt.cc{url}', callback=self.parser_post, cookies={'over18': '1'})

    def parser_post(self, response):
        title = response.xpath('//title/text()').get()
        # print(f'title: {title}')
        item = ScrapyHwItem()
        item['title'] = title
        yield item
