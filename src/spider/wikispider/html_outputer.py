

import sys
class HtmlOutpter(object):
    # 构造方法
    def __init__(self):
        self.datas = []

    # 收集数据的方法
    def collect_data(self, new_datas):
        if new_datas is None:
            return
        # 如果数据不为空就讲数据添加datas集合中c
        self.datas.append(new_datas)

    # 输出爬取到的数据到本地磁盘中
    def out_html(self):
        if self.datas is None:
            return
        
        print(sys.path[0])
       
        file = open(sys.path[0] + '\out.html', 'a', encoding='utf-8')

        file.write("<html>")
        file.write("<head>")
        file.write("<title>爬取结果</title>")
        # 设置表格显示边框
        file.write(r'''
        <style>
         table{width:100%;table-layout: fixed;word-break: break-all; word-wrap: break-word;}
         table td{border:1px solid black;width:300px}
        </style>
        ''')
        file.write("</head>")
        file.write("<body>")
        file.write("<table cellpadding='0' cellspacing='0'>")
        # 遍历datas填充到表格中
        for data in self.datas:
            file.write("<tr>")
            file.write('<td><a href='+str(data['url'])+'>'+str(data['url'])+'</a></td>')
            file.write("<td>%s</td>" % data['title'])
            file.write("<td>%s</td>" % data['summary'])
            file.write("<td>%s</td>" % data['info'])
            file.write("</tr>")
        file.write("</table>")
        
        file.write("</body>")
        file.write("</html>")
    