import os
from py2neo import Graph, Node, Relationship, NodeMatcher
entityDic = dict()
for line in open(os.getcwd() + "../../data/entity.csv"):
    triple = line.strip().split(",")
    entityDic[triple[1]] = triple[0]
graph = Graph('http://localhost:7474', username='neo4j', password='123321')
matcher = NodeMatcher(graph)
propDic = dict(dict())
for line in open(os.getcwd() + "../../data/prop1.txt"):
    triple = line.strip().split("\t")
    if len(triple) != 3:
        triple = line.strip().split(",")
    index = entityDic[triple[0]]
    print(index)
    tmpDic = propDic.get(index, None)
    if tmpDic is None:
        propDic[index] = {triple[1]: triple[2]}
    else:
        tmpstr = propDic[index].get(triple[1], "")
        if tmpstr == "":
            propDic[index][triple[1]] = triple[2]
        else:
            propDic[index][triple[1]] = tmpstr+"<;>"+triple[2]
    print(propDic[index])
count = 0
total = len(propDic)
for index in propDic:
    p = matcher.match(entity=index).first()
    for prop in propDic[index]:
        p[prop] = propDic[index][prop]
    graph.push(p)
    count += 1
    print(index, count, count/total)
'''
count = 0
for line in open(os.getcwd() + "../../data/prop1.txt"):
    triple = line.strip().split("\t")
    if len(triple) != 3:
        triple = line.strip().split(",")
    count += 1
    print(count)
    # print(triple)
    print(entityDic[triple[0]])
    p = matcher.match(entity=entityDic[triple[0]]).first()
    # print(type(p))
    if p[triple[1]] is None:
        p[triple[1]] = triple[2]
    else:
        p[triple[1]] += "<;>"+triple[2]
    graph.push(p)
'''
