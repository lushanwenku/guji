from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from guji.spiders.newdu_spider import NewduSpider

if __name__ == '__main__':

    # 通过方法 get_project_settings() 获取配置信息
    process = CrawlerProcess(get_project_settings())
    process.crawl(NewduSpider)
    process.start()
