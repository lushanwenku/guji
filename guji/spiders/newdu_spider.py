import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
crawler = CrawlerProcess(settings)


class NewduSpider(scrapy.Spider):
    name = 'newdu'
    allowed_domains = ['newdu.com']
    start_urls = ['http://ab.newdu.com/book/']

    def parse(self, response):
        pass
