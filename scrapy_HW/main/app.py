from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():

    url_list = [
        'https://www.ptt.cc/bbs/Gossiping/M.1581055706.A.1EB.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581055788.A.7BC.html'
    ]

    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler2', start_urls=url_list)
    process.start()




if __name__ == '__main__':
    main()
