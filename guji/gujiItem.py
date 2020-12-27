# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GujiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #ID = scrapy.Field()
    post_author = scrapy.Field()
    post_date = scrapy.Field()
    post_date_gmt = scrapy.Field()
    post_content = scrapy.Field()
    post_title = scrapy.Field()
    post_excerpt = scrapy.Field()
    post_status = scrapy.Field()
    comment_status = scrapy.Field()
    ping_status = scrapy.Field()
    post_password = scrapy.Field()
    post_name = scrapy.Field()
    to_ping = scrapy.Field()
    pinged = scrapy.Field()
    post_modified = scrapy.Field()
    post_modified_gmt = scrapy.Field()
    post_content_filtered = scrapy.Field()
    post_parent = scrapy.Field()
    guid = scrapy.Field()
    menu_order = scrapy.Field()
    post_type = scrapy.Field()
    post_mime_type = scrapy.Field()
    comment_count = scrapy.Field()

    # 非数据库字段
    # 类型:一级
    cate_one_name = scrapy.Field()
    # 类型：二级
    post_term = scrapy.Field()
    # 简介
    post_description = scrapy.Field()
    # 章节名
    book_chapter_name = scrapy.Field()
    # 作者名
    post_author_name = scrapy.Field()

    pass
