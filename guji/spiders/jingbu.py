import scrapy

from guji.gujiItem import GujiItem


class Jingbu(scrapy.Spider):
    name = 'jingbu'
    allowed_domains = ['newdu.com']
    start_urls = ['http://ab.newdu.com/book/list-1-1.html']
    newdu_url = 'http://ab.newdu.com'

    def parse(self, response):
        for book_url in response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/@href').extract():
            yield scrapy.Request(self.newdu_url+book_url, callback=self.parse_catalog_url)

        next_url = response.xpath('//*[@id="dedePageList"]/dd[9]/a/@href').extract()
        if next_url:
            yield scrapy.Request(self.newdu_url+next_url[0],callback=self.parse)

    def parse_catalog_url(self,response):
        # post_title = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[1]/div[2]/h1/a[1]/text()').extract()
        # post_author = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h2[1]/text()').extract()
        # post_type = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h2[2]/a/text()').extract()
        # book_catalog_title = response.xpath('//*[@id="chapterlist"]/dd[1]/a/text()').extract()
        book_catalog_url = response.xpath('//*[@id="chapterlist"]/dd/a/@href').extract()
        for catalog_url in book_catalog_url:
            yield scrapy.Request(self.newdu_url+catalog_url,callback=self.parse_content)

    def parse_content(self,response):
        post_content = response.xpath('//*[@id="book_middle"]/div[1]/div[2]/dl/dd').extract()[0]
        print("=========:"+post_content)
        item = GujiItem()
        yield item