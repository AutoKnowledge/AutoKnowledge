import sys
import csv
class Output(object):
    # 构造方法
    def __init__(self):
        self.datas = []

    # 收集数据的方法
    def collect_data(self, new_datas):
        if new_datas is None:
            return
        # 如果数据不为空就讲数据添加datas集合中
        self.datas.append(new_datas)
    # 输出爬取到的数据到本地磁盘中
    def out(self):
        if self.datas is None:
            return
        csv_file = open(sys.path[0] + '/out.csv', 'w', encoding='utf-8')
        writer = csv.writer(csv_file)
        writer.writerow(['url', 'title', 'summary','info'])
        for data in self.datas:
            data_to_write = [
                (data['url'], data['title'],data['summary'],data['info']),
               
                ]
            writer.writerows(data_to_write)