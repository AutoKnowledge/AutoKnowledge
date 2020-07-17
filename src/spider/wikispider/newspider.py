


# 爬虫入口调度器
import url_manager
import html_downloader
import html_parser
import html_outputer


from urllib.parse import quote
import urllib
import  string

class SpiderMain(object):
    def __init__(self):
        self.urlManager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmpParser()
        #self.output = output.Output()
        self.output = html_outputer.HtmlOutpter()


    def craw(self,url):
       
        html_content = self.downloader.download(url)
        new_datas = self.parser.parse(url, html_content)
        self.output.collect_data(new_datas)
        self.output.out_html()

if __name__=="__main__":

    filename='C:\\Users\\ZJCC\\Desktop\\kg\\spider\\newspider\\1.txt'

    lines = []
    with open(filename, 'r',encoding="utf-8") as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)

    for l in lines:
       
        name=urllib.parse.quote(l)
        name.encode('utf-8')
        url='http://baike.baidu.com/search/word?word='+name

        print(url)
   
        sm = SpiderMain()
        sm.craw(url)