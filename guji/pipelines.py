# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pypinyin
from itemadapter import ItemAdapter

from guji.utils.mysql import MySQL


class GujiPipeline:
    def __init__(self):
        self.mysql = MySQL()

    def hp(self,word):
        s = ''
        for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
            s += ''.join(i)
        return s

    def process_item(self, item, spider):
        # 分类：一级 如：经部
        cate_one_id_sql = "select a.* from wp_terms a where a.name = '{name}'".format(name=item['cate_one_name'])
        cate_one_id = self.mysql.get_one(cate_one_id_sql)[0]

        # 分类：二级 如：易类
        term_id = 0
        wp_terms_name = item['post_term']
        term_id_sql = "select a.* from wp_terms a where a.name = '{name}'".format(name=wp_terms_name)
        term_id_tup = self.mysql.get_one(term_id_sql)

        #判断二级分类是否存在
        if term_id_tup:
            term_id = term_id_tup[0]
            print(term_id)
        else:
            wp_terms_data = {'name':wp_terms_name,'slug':self.hp(wp_terms_name),'term_group':0}
            term_id = self.mysql.insert('wp_terms',wp_terms_data)

            # 一级和二级 分类 添加关联
            # wp_term_taxonomy( term_id, taxonomy, description, parent, count) VALUES (17, 17, 'post_tag', '', 0, 1);
            wp_term_taxonomy_data = {'term_id':term_id,'taxonomy':'category','description':'','parent':cate_one_id,'count':0}
            self.mysql.insert('wp_term_taxonomy',wp_term_taxonomy_data)

            #二级 导航菜单
            nav_menu_item_two_data = {'post_author':6,'post_parent':cate_one_id}
            nav_menu_item_two_sql = "INSERT INTO wp_posts ( post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count )VALUES({post_author},'2020-12-29 00:00:00','2020-12-29 00:00:00','','','','publish','closed','closed','','','','','2020-12-29 00:00:00','2020-12-29 00:00:00','',{post_parent},'',0,'nav_menu_item','',0)".format(**nav_menu_item_two_data)
            nav_menu_item_id = self.mysql.insert_sql(nav_menu_item_two_sql)

            #二级 导航菜单 和 菜单分类 关联
            wp_term_relationships_data = {'object_id':nav_menu_item_id,'term_taxonomy_id':5}
            wp_term_relationships_sql = "INSERT INTO wp_term_relationships(object_id, term_taxonomy_id, term_order) VALUES ({object_id}, {term_taxonomy_id}, 0)".format(**wp_term_relationships_data)
            wp_term_relationships_id = self.mysql.insert_sql(nav_menu_item_two_sql)
            #

        pass

        cate_one_name = item['cate_one_name']
        post_term = item['post_term']
        post_description = item['post_description']
        book_chapter_name = item['book_chapter_name']
        post_author_name = item['post_author_name']
        item.pop('cate_one_name')
        item.pop('post_term')
        item.pop('post_description')
        item.pop('book_chapter_name')
        item.pop('post_author_name')
        #print(item)
        wp_posts_id = self.mysql.insert('wp_posts',item)
        item['cate_one_name'] = cate_one_name
        item['post_term'] = post_term
        item['post_description'] = post_description
        item['book_chapter_name'] = book_chapter_name
        item['post_author_name'] = post_author_name

        #文章和二级分类关联
        wp_term_relationships_data = {'object_id':wp_posts_id,'term_taxonomy_id':term_id,'term_order':0}
        self.mysql.insert('wp_term_relationships',wp_term_relationships_data)

        return item
