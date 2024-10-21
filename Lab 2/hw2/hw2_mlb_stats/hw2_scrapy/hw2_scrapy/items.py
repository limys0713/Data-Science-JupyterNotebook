# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hw2ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    PLAYER = scrapy.Field()
    TEAM = scrapy.Field()
    G = scrapy.Field()
    AB = scrapy.Field()
    R = scrapy.Field()
    H = scrapy.Field()
    HR = scrapy.Field()
    RBI = scrapy.Field()
    BB = scrapy.Field()
    SO = scrapy.Field()
    SB = scrapy.Field()
    AVG = scrapy.Field()
    OBP = scrapy.Field()
    SLG = scrapy.Field()
    
    pass
