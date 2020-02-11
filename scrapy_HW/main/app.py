from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():

    url_list = [
        'https://www.ptt.cc/bbs/Gossiping',
        'https://www.ptt.cc/bbs/NBA'
    ]

    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler2', start_urls=url_list)
    process.start()




if __name__ == '__main__':
    main()
