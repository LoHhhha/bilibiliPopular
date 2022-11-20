# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibilipopularItem(scrapy.Item):
    # 捕获时间
    video_catch_time = scrapy.Field()  # String
    # 视频标题
    video_title = scrapy.Field()  # String
    # 作者
    author_name = scrapy.Field()  # String
    # 视频链接
    video_url = scrapy.Field()  # String
    # 视频封面
    video_picture = scrapy.Field()  # String
    # 视频标签
    video_type = scrapy.Field()  # String
    # 视频简介
    video_desc = scrapy.Field()  # String
    # 热门原因
    why_popular = scrapy.Field()  # String
    # 视频数据
    video_view = scrapy.Field()  # Int
    video_favorite = scrapy.Field()  # Int
    video_reply = scrapy.Field()  # Int
    video_coin = scrapy.Field()  # Int
    video_share = scrapy.Field()  # Int
    video_like = scrapy.Field()  # Int
    # 附加推荐视频
    recommend_video = scrapy.Field()  # List [{'video_name': xx, 'video_url': xx}]
