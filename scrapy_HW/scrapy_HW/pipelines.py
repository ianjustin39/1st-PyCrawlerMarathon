# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ScrapyHwPipeline(object):

    def open_spider(self, spider):
        self.output_file = open('items.json', 'w')

    def close_spider(self, spider):
        self.output_file.close()

    def process_item(self, item, spider):
        data = {
            'title': item.get('title')
        }
        self.output_file.write(json.dumps(data, ensure_ascii=False))
        return item
