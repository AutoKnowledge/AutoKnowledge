#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import csv
import os
import numpy as np

propf = open("prop.txt", "w")
h_r_t = {":START_ID": [], "role": [], ":END_ID": []}

csvFile = open("Disease.csv", "r")
reader = csv.reader(csvFile)
for item in reader:
    if len(item) != 3:
        print(item)
        continue
    item[2] = item[2].replace("\n", "")
    item[2] = item[2].replace(",", "，")
    if len(item[2]) > 32:
        propf.write(item[0]+','+item[1]+','+item[2]+'\n')
        continue
    h_r_t[":START_ID"].append(item[0])
    h_r_t["role"].append(item[1])
    h_r_t[":END_ID"].append(item[2])

csvFile.close()
propf.close()
# 去除重复实体
entity = set()
entity_h = h_r_t[':START_ID']
entity_t = h_r_t[':END_ID']
for i in entity_h:
    entity.add(i)

for i in entity_t:
    entity.add(i)


# 保存节点文件
csvf_entity = open("entity.csv",
                   "w", newline='', encoding='utf-8')

csvf_entity.write("entity:ID, name"+"\n")
entity = list(entity)
entity_dict = {}
for i in range(len(entity)):
    csvf_entity.write("e"+str(i)+","+entity[i]+"\n")
    entity_dict[entity[i]] = "e"+str(i)
csvf_entity.close()
np.save('entity_id.npy', entity_dict)

csvf_relation = open("relation.csv",
                     "w", newline='', encoding='utf-8')
csvf_relation.write(":START_ID,:END_ID,:TYPE\n")


for h, t, r in zip(h_r_t[':START_ID'], h_r_t[':END_ID'], h_r_t['role']):
    try:
        csvf_relation.write(entity_dict[h]+"," + entity_dict[t]+"," + r+"\n")
    except:
        print(h, t, r)
csvf_relation.close()
'''
./neo4j-import --into /home/xiaopeng/Downloads/neo4j-community-3.5.13/data/databases/graph.db --nodes /home/xiaopeng/Desktop/AutoKnowledge/data/entity.csv --relationships /home/xiaopeng/Desktop/AutoKnowledge/data/roles.csv
'''
'''
# Save
dictionary = {'hello':'world'}
np.save('my_file.npy', dictionary) 

# Load
read_dictionary = np.load('my_file.npy').item()
print(read_dictionary['hello']) # displays "world"
'''
