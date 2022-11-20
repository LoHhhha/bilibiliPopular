import re

import requests
from bs4 import BeautifulSoup

# source = requests.get(url="https://api.bilibili.com/x/web-interface/popular?ps=1&pn=1")
# popular_data = source.json()['data']
#
# video_data = popular_data['list'][0]
# print(video_data)
# # 视频标题
# video_title = video_data['title']
# print(video_title)
# # 作者
# author_name = video_data['owner']['name']
# print(author_name)
# # 视频链接
# video_url = video_data['short_link']
# print(video_url)
# # 视频封面
# video_picture = video_data['pic']
# print(video_picture)
# # 视频标签
# video_type = video_data['tname']
# print(video_type)
# # 视频简介
# video_desc = video_data['desc']
# print(video_desc)
# # 热门原因
# why_popular = video_data['rcmd_reason']['content']
# print(why_popular)
# # 视频数据
# video_view = video_data['stat']['view']
# print(video_view)
# video_favorite = video_data['stat']['favorite']
# print(video_favorite)
# video_reply = video_data['stat']['reply']
# print(video_reply)
# video_coin = video_data['stat']['coin']
# print(video_coin)
# video_share = video_data['stat']['share']
# print(video_share)
# video_like = video_data['stat']['like']
# print(video_like)
# # 附加推荐视频
# # recommend_video = scrapy.Field()  # List [{'video_name': xx, 'video_url': xx}]
#
# page_source = requests.get(url=video_url).content
# bs = BeautifulSoup(page_source, 'lxml')
# for video in bs.find_all(name='div', attrs={'class': 'info'}):
#
#     if video.a:
#         # print(video)
#         print(video.p['title'])
#         try:
#             video.a['target']
#         except KeyError:
#             cur_recommend_video = "https://www.bilibili.com"+re.findall(r'/video/[0-9A-Za-z]*/', video.a['href'])[0]
#             print(cur_recommend_video)

# import datetime
# import os
#
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# date = datetime.datetime.now().strftime("%Y-%m-%d")
# path = './Data/'+date
# if not os.path.exists(path):
#     os.makedirs(path)

name = '\\<>?|*/"'
name = name.replace('\\', '_').replace('/', '_').replace('<', '《').replace('>', '》').replace('|', '_')\
    .replace('*', '#').replace('?', '？').replace('"', "'")
print(name)
