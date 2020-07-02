import os
from py2neo import Graph, Node, Relationship, NodeMatcher, PropertyDict
import time
import random

id2entityDic = dict()
entity2idDic = dict()
for line in open(os.getcwd() + "/../data/entity.csv"):
    triple = line.strip().split(",")
    id2entityDic[triple[0]] = triple[1]
    entity2idDic[triple[1]] = triple[0]
graph = Graph('http://localhost:7474', username='neo4j', password='123321')


def hr2t(entityID, relationType):
    return "MATCH p=(h)-[r:`"+relationType+"`]->(t) where id(h)="+entityID+" RETURN t"


def ht2r(entityID_h, entityID_t):
    return "MATCH p=(h)-[r]->(t) where id(h)="+entityID_h+" and id(t)="+entityID_t + " RETURN r"


def rt2h(entityID, relationType):
    return "MATCH p=(h)-[r:`"+relationType+"`]->(t) where id(t)="+entityID+" RETURN h"


def h2r(entityID):
    return "MATCH p=(h)-[r]->(t) where id(h)="+entityID+" RETURN r"


def t2r(entityID):
    return "MATCH p=(h)-[r]->(t) where id(t)="+entityID+" RETURN r"


'''
time1 = time.process_time()
p = graph.run(rt2h("e4095675", "分子式"))
for record in p:
    entityID = record.values()[0]["entity"]
    print(id2entityDic[entityID])

p = graph.run(hr2t("e6817387", "分子式"))
for record in p:
    entityID = record.values()[0]["entity"]
    print(id2entityDic[entityID])

p = graph.run(ht2r("e6817387", "e4095675"))
for record in p:
    print(record.values()[0].__class__.__name__)

p = graph.run(h2r("e6817387"))
for record in p:
    print(record.values()[0].__class__.__name__)
time2 = time.process_time()
print(time1, time2)
'''

# （）的{关系}是{尾实体}?


def findHead(entityID, count=1):
    relations = []
    p = graph.run(h2r(entityID))
    for reltion in p:
        relations.append(reltion.values()[0].__class__.__name__)
    selectRelation = relations[random.randint(0, len(relations)-1)]
    tails = []
    p = graph.run(hr2t(entityID, selectRelation))
    for tail in p:
        tails.append(id2entityDic[tail.values()[0]["entity"]])
    selectTail = tails[random.randint(0, len(tails)-1)]
    # print(id2entityDic[entityID]+"的"+selectRelation+"是"+selectTail)
    question = "（   ）的"+selectRelation+"是"+selectTail
    print([question, [id2entityDic[entityID], 'b', 'c', 'd']], ['A'])
    return [question, [id2entityDic[entityID], 'b', 'c', 'd']], ['A']
# {头实体}的{关系}是()?单选 || {头实体}的{关系}有()?


def findTail(entityID):
    relations = []
    p = graph.run(h2r(entityID))
    for reltion in p:
        relations.append(reltion.values()[0].__class__.__name__)
    selectRelation = relations[random.randint(0, len(relations)-1)]
    p = graph.run(hr2t(entityID, selectRelation))
    tails = set()
    for tail in p:
        tails.add(id2entityDic[tail.values()[0]["entity"]])
    tails = list(tails)
    flag = False
    if len(tails) > 1:
        flag = True
    count = random.randint(1, len(tails))
    if count > 4:
        count = 4
    if flag:
        question = id2entityDic[entityID]+"的"+selectRelation+"有(   )"
    else:
        question = id2entityDic[entityID]+"的"+selectRelation+"是(   )"
    option = ['a', 'b', 'c', 'd']
    answer = []
    for i in range(count):
        selectTail = tails[random.randint(0, len(tails)-1)]
        option[i] = selectTail
        answer.append(chr(ord('A')+i))
    print([question, option], answer)
    return [question, option], answer


def get_question(entity=""):
    while True:
        try:
            classID = random.randint(0, 1)
            #entityID = "e"+str(random.randint(0, 5000000))
            entityID = str(random.randint(0, 5000000))
            if classID:
                return findTail(entityID)
            else:
                return findHead(entityID)
        except:
            pass



'''
while True:
    input()
    print("start")
    time1 = time.time()
    get_question()
    time2 = time.time()
    print(time2-time1)
'''