#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import csv
import os

h_r_t = {":START_ID": [], "role": [], ":END_ID": []}
for line in open(os.getcwd() + "/../data/pure_baike_triples.txt"):
    triple = line.strip().split("\t")
    if len(triple) != 3:
        print(triple)
        continue
    h_r_t[":START_ID"].append(triple[0])
    h_r_t["role"].append(triple[1])
    h_r_t[":END_ID"].append(triple[2])

prop = set()
# 去除重复实体
entity = set()
entity_h = h_r_t[':START_ID']
entity_t = h_r_t[':END_ID']
for i in entity_h:
    entity.add(i)
entity_t_dict = dict()
for i in entity:
    entity_t_dict[i] = 101
for i in entity_t:
    entity_t_dict[i] = entity_t_dict.get(i, 0)+1
for i in entity_t_dict:
    if entity_t_dict[i] > 100:
        entity.add(i)
    else:
        prop.add(i)
print(len(entity))
del entity_t_dict
# 保存节点文件
csvf_entity = open(os.getcwd() + "/../data/entity.csv",
                   "w", newline='', encoding='utf-8')

csvf_entity.write("entity:ID, name"+"\n")
entity = list(entity)
entity_dict = {}
for i in range(len(entity)):
    csvf_entity.write("e"+str(i)+","+entity[i]+"\n")
    entity_dict[entity[i]] = "e"+str(i)
csvf_entity.close()
del entity
csvf_relation = open(os.getcwd() + "/../data/relation.csv",
                     "w", newline='', encoding='utf-8')
# csvf_relation.write(":START_ID,:END_ID,:TYPE\n")
propf = open(os.getcwd() + "/../data/prop.txt", "w")
for h, t, r in zip(h_r_t[':START_ID'], h_r_t[':END_ID'], h_r_t['role']):
    if t in prop:
        propf.write(h+"\t"+r+"\t"+t+"\n")
        continue
    else:
        csvf_relation.write(entity_dict[h]+"," + entity_dict[t]+"," + r+"\n")
csvf_relation.close()
for line0 in open(os.getcwd() + "/../data/baike_triples.txt"):
    triple = line0.strip().split("\t")
    if len(triple) != 3 or triple[1] != "BaiduCARD":
        continue
    line = line0.replace("<a>", "")
    line = line.replace("</a>", "")
    line = line.replace("\"\"", "")
    line = line.replace("\\\"", "”")
    line = line.replace("\"", "”")
    line = line.replace(",", "，")
    propf.write(line)
propf.close()
'''
./neo4j-import --into /home/xiaopeng/Downloads/neo4j-community-3.5.13/data/databases/graph.db --nodes /home/xiaopeng/Desktop/AutoKnowledge/data/entity.csv --relationships /home/xiaopeng/Desktop/AutoKnowledge/data/roles.csv
'''
