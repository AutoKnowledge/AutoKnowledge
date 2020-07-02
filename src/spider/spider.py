# 爬虫的入口调度器
import url_manager
import html_downloader
import html_parser
import output


class SpiderMain(object):
    def __init__(self):
        self.urlManager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmpParser()
        self.output = output.Output()


    def craw(self,url):
        count = 1 #定义爬取几个页面
        self.urlManager.add_new_url(url)
        while self.urlManager.has_new_url():
            try:
                # 获取一个url
                new_url = self.urlManager.get_new_url()
                # 访问url，获取网站返回数据
                html_content = self.downloader.download(new_url)
                new_urls, new_datas = self.parser.parse(new_url, html_content)
                self.urlManager.add_new_urls(new_urls)
                self.output.collect_data(new_datas)
                print(count)
                if count == 10:
                    break
                count = count+1
            except Exception as e:
                print("发生错误",e)
        # 将爬取结果输出到html
        self.output.out()

if __name__=="__main__":
    url = 'https://baike.baidu.com/item/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/25279'
    sm = SpiderMain()
    sm.craw(url)