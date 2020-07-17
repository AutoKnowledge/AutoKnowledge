
# url管理器
class UrlManager(object):
    def __init__(self):
        # 定义两个set，一个存放未爬取的url，一个爬取已经访问过的url
        self.new_urls = set()
        self.old_urls = set()

    # 添加一个url的方法
    def add_new_url(self,url):
        if url is None:
            return  None
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 判断是否还有待爬取的url(根据new_urls的长度判断是否有待爬取的页面)
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 定义获取一个新的url的方法
    def get_new_url(self):
        if len(self.new_urls)>0:
            # 从new_urls弹出一个并添加到old_urls中
            new_url = self.new_urls.pop()
            self.old_urls.add(new_url)
            return new_url

    # 批量添加url的方法
    def add_new_urls(self, new_urls):
        if new_urls is None:
            return
        for url in new_urls:
            self.add_new_url(url)