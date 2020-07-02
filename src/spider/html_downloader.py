# 读取网页的类
import urllib.request


class HtmlDownLoader(object):
    def download(self, url):
        if url is None:
            return
        # 访问url
        response = urllib.request.urlopen(url)
        # 如果返回的状态码不是200代表异常

       
        if response.getcode() != 200:
            return
        return response.read()