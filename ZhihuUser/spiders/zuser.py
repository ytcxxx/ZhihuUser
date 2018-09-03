# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request

from ZhihuUser.items import UserItem


class ZuserSpider(scrapy.Spider):
    name = "zuser"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']
    
    start_user = 'excited-vczh'
    
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    
    follow_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follow_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    
    follower_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    follower_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    
    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse)
        yield Request(self.follow_url.format(user=self.start_user, include=self.follow_query, offset=20, limit=20), callback=self.parse_follow)
        yield Request(self.follower_url.format(user=self.start_user, include=self.follower_query, offset=20, limit=20), callback=self.parse_follower)
        
    def parse(self, response):
        results = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in results.keys():
                item[field] = results.get(field)
                yield item
                yield Request(self.follow_url.format(user=results.get('url_token'), include=self.follow_query, offset=20, limit=20), self.parse_follow)
                yield Request(self.follower_url.format(user=results.get('url_token'), include=self.follower_query, offset=20, limit=20), self.parse_follower)
    
    def parse_follow(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), callback=self.parse)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, callback=self.parse_follow)
            
    def parse_follower(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), callback=self.parse)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, callback=self.parse_follower)