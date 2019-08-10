# url_manager.py
class UrlManager(object):
    def __init__(self):  # url管理器里面需要两个set来分别记录已经爬去的类和未爬取的类
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):  # 如果待添加的url为有效的url，且该url即不在已爬去的set里，也不在未爬去的set里，则添加
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):  # 对于添加一堆的url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):  # 检查是否还有未爬取的url。
        return len(self.new_urls) != 0

    def get_new_url(self):  # 从未爬取的url set中取出一个url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
