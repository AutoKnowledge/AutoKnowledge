# 网页解析器类
import re
import urllib

from bs4 import BeautifulSoup


class HtmpParser(object):
    # 解析读取到的网页的方法
    def parse(self, new_url, html_content):
        if html_content is None:
            return
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        new_urls = self.get_new_urls(new_url,soup)
        new_datas = self.get_new_datas(new_url,soup)

        return new_urls, new_datas


    # 获取new_urls的方法
    def get_new_urls(self, new_url, soup):
        new_urls = set()
        # 查找网页的a标签，而且href包含/item
        #links = soup.find_all('a',href=re.compile(r'/item'))
        links = soup.find('div',attrs = {'class':'lemma-summary'}).find_all("a")
        #print(links)
        for link in links:
            #print("ok")
            #print(link.get("href"))
            url = link['href']
            # 合并url。使爬到的路径变为全路径，http://....的格式
            new_full_url = urllib.parse.urljoin(new_url,url)
            new_urls.add(new_full_url)
        return new_urls



    # 获取new_data的方法
    def get_new_datas(self, new_url, soup):
        new_datas = {}
        # 获取标题内容
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_datas['title'] = title_node.get_text()

        #获取内容
        summary_node = soup.find('div',class_='lemma-summary')
        new_datas['summary'] = summary_node.get_text()
        summary_node = soup.find('div',class_='basic-info cmn-clearfix')
        new_datas['info'] = summary_node.get_text()
        new_datas['url'] = new_url

        


        return new_datas