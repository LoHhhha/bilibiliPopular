# bilibili热门视频信息捕获

## 1. 运行环境
    Python3.9.12

## 2. 库版本
    Scrapy 2.7.1
    requests 2.27.1
    beautifulsoup4 4.11.1

## 3. 功能
爬取当前时间节点下哔哩哔哩热门视频的信息，包括但不限于：
* 视频标题
* 视频作者
* 视频标签
* 视频简介
* 视频数据
* 视频页面下推荐视频

## 4. 文件结构
    - root
        - bilibiliPopular
            - bilibiliPopular
                - spiders
        - Data


## 4. 运行

### I. 终端进入bilibiliPopular目录

    cd xxx\bilibili热门数据爬取\bilibiliPopular

### II. 终端执行

    scrapy crawl bilibili

### III. 数据查看

数据位于Data目录下
