# html_downloader.py

import string
import urllib
from urllib import request
from urllib.parse import quote


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        if url is None:
            return None

        url_ = quote(url, safe=string.printable)  # 这个主要应对中文编码的问题。
        # url = "http://blog.csdn.net/hurmishine/article/details/71708030"
        req = urllib.request.Request(url_)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
        data = urllib.request.urlopen(req).read().decode('utf-8')

        return data
        # response = request.urlopen(url_)
        #
        # if response.getcode() != 200:  # 判断是否正常访问该网页
        #     return None
        #
        # return response.read()
