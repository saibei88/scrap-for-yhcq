# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YhcqItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    volume = scrapy.Field()
    content = scrapy.Field()
    news_id = scrapy.Field()
    page = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    url = scrapy.Field()
    volumename = scrapy.Field()

class YhcqVolumeItem(scrapy.Item):
    # define the fields for your item here like:
    volume = scrapy.Field()
    intro = scrapy.Field()
    preface = scrapy.Field()
    volumename = scrapy.Field()
