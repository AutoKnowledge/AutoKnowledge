import os
from py2neo import Graph, Node, Relationship, NodeMatcher
import numpy as np
entityDic = np.load("entity_id.npy", allow_pickle=True).item()

graph = Graph('http://localhost:7474', username='neo4j', password='123321')
matcher = NodeMatcher(graph)
propDic = dict(dict())
for line in open("prop.txt"):
    triple = line.strip().split(",")
    if len(triple) != 3:
        continue
    index = entityDic[triple[0]]
    propDic[index] = {triple[1]: triple[2]}

count = 0
total = len(propDic)
for index in propDic:
    p = matcher.match(entity=index).first()
    for prop in propDic[index]:
        p[prop] = propDic[index][prop]
    graph.push(p)
    count += 1
    print(index, count, count/total)
