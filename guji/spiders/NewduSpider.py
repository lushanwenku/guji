import scrapy


class NewduSpider(scrapy.Spider):
    name = 'newdu'
    allowed_domains = ['newdu.com']
    start_urls = ['http://ab.newdu.com/']

    def parse(self, response):
        pass
