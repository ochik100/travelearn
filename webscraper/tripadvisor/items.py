# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field


class StateTopicItem(Item):
    state = Field()
    topic = Field()
    topic_url = Field()
    # creator = Field()
    posts = Field()


class StateItem(Item):
    state = Field()
    url = Field()
    num_topics = Field()
    num_posts = Field()
    state_topic = Field()


class PostItem(Item):
    state = Field()
    topic = Field()
    date_time = Field()
    user = Field()
    user_location = Field()
    text = Field()