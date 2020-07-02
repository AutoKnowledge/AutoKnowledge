# AutoKnowledge
工程实践
# 执行顺序
cleanBaiketxt.py //去除原文件中的英文逗号和引号，删除<a>和<\a>，剔除BaidCARD
csv2neodata.py //将尾结点出现次数少于100的三元组定义为属性并加入BaiduCARD，保存为prop.txt
getRelations.py //统计relation.csv中关系出现的次数
cleanRelation.py //关系出现次数少于10的三元组保存到属性文件prop1.txt
将prop1.txt追加到prop.txt
prop2json.py //将prop.txt文件转为json形式