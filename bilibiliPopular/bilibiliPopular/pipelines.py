import datetime
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BilibilipopularPipeline:
    path = None

    def open_spider(self, spider):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.path = './Data/' + date
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def process_item(self, item, spider):
        # 文件名有效化
        name = item['video_title']
        name = name.replace('\\', '_').replace('/', '_').replace('<', '《').replace('>', '》').replace('|', '_') \
            .replace('*', '#').replace('?', '？').replace('"', "'")
        save_path = self.path + '/' + name + '.txt'

        with open(save_path, 'w', encoding='utf-8') as fp:
            fp.write('更新时间：' + item['video_catch_time'] + '\n' + '\n')
            fp.write('视频标题：' + item['video_title'] + '\n')
            fp.write('视频作者：' + item['author_name'] + '\n')
            fp.write('视频链接：' + item['video_url'] + '\n')
            fp.write('视频封面：' + item['video_picture'] + '\n')
            fp.write('视频标签：' + item['video_type'] + '\n' + '\n')
            fp.write('视频简介：' + item['video_desc'] + '\n' + '\n')
            fp.write('热门原因：' + item['why_popular'] + '\n' + '\n')
            fp.write('视频数据：' + '\n')
            fp.write('点赞：' + str(item['video_like']) + '\n')
            fp.write('投币：' + str(item['video_coin']) + '\n')
            fp.write('转发：' + str(item['video_share']) + '\n')
            fp.write('评论：' + str(item['video_reply']) + '\n')
            fp.write('收藏：' + str(item['video_favorite']) + '\n' + '\n')
            fp.write('该视频下推荐视频：' + '\n')
            for video in item['recommend_video']:
                fp.write('\t视频标题：' + video['video_name'] + '\n')
                fp.write('\t' + video['video_url'] + '\n')
        return item
