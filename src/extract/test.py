'''
import analyze
any = analyze.Analyze()
# 吻别是由张学友演唱的一首歌曲。
#text = '《盗墓笔记》是2014年欢瑞世纪影视传媒股份有限公司出品的一部网络季播剧，改编自南派三叔所著的同名小说，由郑保瑞和罗永昌联合导演，李易峰、杨洋、唐嫣、刘天佐、张智尧、魏巍等主演。'
#text = '姚明1980年9月12日出生于上海市徐汇区，祖籍江苏省苏州市吴江区震泽镇，前中国职业篮球运动员，司职中锋，现任中职联公司董事长兼总经理。'
knowledge = any.knowledge(text)
print(knowledge)
'''
from medext import getTriples
text = "据报道称，新冠肺炎患者经常会发热、咳嗽，少部分患者会胸闷、=乏力，其病因包括: 1.自身免疫系统缺陷 2.人传人。"
#text = "少部分先天性心脏病在5岁前有自愈的机会，另外有少部分患者畸形轻微、对循环功能无明显影响，而无需任何治疗，但大多数患者需手术治疗校正畸形。随着医学技术的飞速发展，手术效果已经极大提高，目前多数患者如及时手术治疗，可以和正常人一样恢复正常，生长发育不受影响，并能胜任普通的工作、学习和生活的需要。"
result = getTriples(text)
print(result)
