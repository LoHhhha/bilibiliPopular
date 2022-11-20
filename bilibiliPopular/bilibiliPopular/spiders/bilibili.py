import scrapy
import requests
import re
import datetime
from bs4 import BeautifulSoup

from ..items import BilibilipopularItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    # allowed_domains = ['xxx.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/popular?ps=50&pn=1']

    url = 'https://api.bilibili.com/x/web-interface/popular?ps=50&pn=%d'
    page_num = 1
    # 规定最大爬取页数
    max_page_num = 3

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52 '
    }

    def parse(self, response):
        # response.json()包含50条热门信息
        popular_data = response.json()['data']
        print("Checking ", self.page_num, " page.")
        for video_data in popular_data['list']:
            item = BilibilipopularItem()
            # 捕获时间
            item['video_catch_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 视频标题
            item['video_title'] = video_data['title']
            # 作者
            item['author_name'] = video_data['owner']['name']
            # 视频链接
            item['video_url'] = video_data['short_link']
            # 视频封面
            item['video_picture'] = video_data['pic']
            # 视频标签
            item['video_type'] = video_data['tname']
            # 视频简介
            item['video_desc'] = video_data['desc']
            # 热门原因
            item['why_popular'] = video_data['rcmd_reason']['content']
            # 视频数据
            item['video_view'] = video_data['stat']['view']
            item['video_favorite'] = video_data['stat']['favorite']
            item['video_reply'] = video_data['stat']['reply']
            item['video_coin'] = video_data['stat']['coin']
            item['video_share'] = video_data['stat']['share']
            item['video_like'] = video_data['stat']['like']

            video_page_source = requests.get(url=video_data['short_link'], headers=self.headers).content
            bs = BeautifulSoup(video_page_source, 'lxml')
            recommend_video = []
            for cur_recommend_video in bs.find_all(name='div', attrs={'class': 'info'}):
                if cur_recommend_video.a:
                    try:
                        # 这一步不出错一定是广告
                        cur_recommend_video.a['target']
                    except KeyError:
                        cur_recommend_video_url = "https://www.bilibili.com" + \
                                                  re.findall(r'/video/[0-9A-Za-z]*/', cur_recommend_video.a['href'])[0]
                        recommend_video.append(
                            {'video_name': cur_recommend_video.p['title'], 'video_url': cur_recommend_video_url})

            # 附加推荐视频
            item['recommend_video'] = recommend_video
            print('Get! ' + video_data['title'])
            yield item
        if (not popular_data['no_more']) and self.page_num <= self.max_page_num:
            # 调用Request并设置回调函数完成全站爬取
            self.page_num += 1
            yield scrapy.Request(url=self.url.format(self.page_num), callback=self.parse)
