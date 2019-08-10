# spider_main.py
import app_html_parser
import html_downloader
import html_outputer
# import html_parser
import url_manager
import json


class SpiderMain(object):
    def __init__(self):  # 初始化
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = app_html_parser.AppHtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, r_url, total_count, processer):
        count = 1
        self.urls.add_new_url(r_url)  # 添加新的url
        while self.urls.has_new_url():  # 检查是否还有新的url
            try:
                new_url = self.urls.get_new_url()  # 获取新的url
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  # 下载该url的编码
                new_urls, new_data = self.parser.parse(new_url, html_cont, processer.get('spider'))  # 用解析器得到新的url和有价值的信息
                self.urls.add_new_urls(new_urls)  # 添加新的url（这里和上面不是同一个函数，因为这里添加的url可能有多个）
                self.outputer.collect_data(new_data)  # 输出有价值的信息

                if count >= total_count:
                    break

                count += 1

            except Exception as e:  # 有可能遇见错误的网页
                print(str(e))
                # 根据报错信息提示错误

            self.outputer.output_html()


if __name__ == '__main__':
    f = open("config1.json", encoding='utf-8')  # 打开文件
    fr = f.read()

    en_json = json.loads(fr)

    # root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'  # 待爬取的网址
    root_url = en_json.get("url")
    obj_spider = SpiderMain()  # 创建爬虫
    obj_spider.craw(en_json.get("url"), 10, en_json)  # 进行抓取
