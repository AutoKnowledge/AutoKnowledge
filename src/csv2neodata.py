#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pandas as pd
import csv
import os
import re
'''
# 读取三元组文件
h_r_t_name = [":START_ID", "role", ":END_ID"]
h_r_t = pd.read_table(
    os.getcwd() + "/../data/pure_baike_triples.txt0", quoting=3, decimal="\t", names=h_r_t_name)
print(h_r_t.info())
print(h_r_t.head())
'''
h_r_t = {":START_ID": [], "role": [], ":END_ID": []}
for line in open(os.getcwd() + "/../data/pure_baike_triples.txt0"):
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
    entity_t_dict[i] = 2
for i in entity_t:
    entity_t_dict[i] = entity_t_dict.get(i, 0)+1
for i in entity_t_dict:
    if entity_t_dict[i] > 1:
        entity.add(i)
    else:
        prop.add(i)
print(len(entity))
# 保存节点文件
csvf_entity = open(os.getcwd() + "/../data/entity.csv",
                   "w", newline='', encoding='utf-8')
# w_entity = csv.writer(csvf_entity)
# 实体ID，要求唯一，名称，LABEL标签，可自己不同设定对应的标签
# w_entity.writerow(("entity:ID", "name"))
csvf_entity.write("entity:ID, name"+"\n")
entity = list(entity)
entity_dict = {}
for i in range(len(entity)):
    #w_entity.writerow(("e" + str(i), "\""+str(entity[i])+"\""))
    csvf_entity.write("e"+str(i)+",<"+entity[i]+">\n")
    entity_dict[entity[i]] = "e"+str(i)
csvf_entity.close()
del entity
csvf_relation = open(os.getcwd() + "/../data/relation.csv",
                     "w", newline='', encoding='utf-8')
#w_relation = csv.writer(csvf_relation)
#w_relation.writerow((":START_ID", ":END_ID", ":TYPE"))
csvf_relation.write(":START_ID,:END_ID,:TYPE\n")
for h, t, r in zip(h_r_t[':START_ID'], h_r_t[':END_ID'], h_r_t['role']):
    if t in prop:
        continue
    else:
        #w_relation.writerow((entity_dict[h], entity_dict[t], r))
        csvf_relation.write(entity_dict[h]+"," + entity_dict[t]+"," + r+"\n")
csvf_relation.close()
'''
# 生成关系文件，起始实体ID，终点实体ID，要求与实体文件中ID对应，:TYPE即为关系
h_r_t[':START_ID'] = h_r_t[':START_ID'].map(entity_dict)
h_r_t[':END_ID'] = h_r_t[':END_ID'].map(entity_dict)
h_r_t[":TYPE"] = h_r_t['role']
h_r_t.pop('role')
h_r_t.to_csv(os.getcwd() + "/../data/roles.csv", index=False)
'''
'''
./neo4j-import --into /home/xiaopeng/Downloads/neo4j-community-3.5.13/data/databases/graph.db --nodes /home/xiaopeng/Desktop/AutoKnowledge/data/entity.csv --relationships /home/xiaopeng/Desktop/AutoKnowledge/data/roles.csv
'''
