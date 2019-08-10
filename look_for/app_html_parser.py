# html_parser.py

import re
import urllib.parse
from bs4 import BeautifulSoup


class AppHtmlParser(object):
    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/"))  # 搜索所有满足条件的url
        # 网址有变，表达式做了调整
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            # Py3中用到的模块名称变为urllib.parse
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup, spider):
        res_data = {'url': page_url}

        # url
        for item in spider:
            rank = soup.select(item.get('selector'))[int(item.get('index'))]
            alis = rank.find_all('div', class_='app-sweatch nofloat')
            for it in alis:
                one = it.find('div', class_='close nofloat')
                title = one.find('a', class_='title').text
                num = one.find('span', class_='num').text
                print(title + num)
            # print(rank)

        # level1 = soup.find('div', class_=' nofloat')
        # level2 = level1.find('', class_='unit-tri flt')

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        # print(title_node.get_text())
        res_data['title'] = title_node.get_text()  # 获取满足条件的标题

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()  # 获取满足条件的信息

        return res_data

    def parse(self, page_url, html_cont, spider):  # 对于下载的页面进行解析
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')  # 先用python自带库进行解析。
        # print(soup.get_text())
        # 提取有用的信息
        new_urls = self._get_new_urls(page_url, soup)  # 提取新的url
        new_data = self._get_new_data(page_url, soup, spider)  # 提取有价值的信息
        return new_urls, new_data
