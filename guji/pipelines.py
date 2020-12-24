# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from guji.utils.mysql import MySQL


class GujiPipeline:
    def __init__(self):
        self.mysql = MySQL()

    def process_item(self, item, spider):
        self.mysql.insert('wp_posts',item)
        return item
