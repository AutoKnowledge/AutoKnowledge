'''
import os
from py2neo import Graph, Node, Relationship, NodeMatcher, PropertyDict, RelationshipMatcher
graph = Graph('http://localhost:7474', username='neo4j', password='123321')
nodematcher = NodeMatcher(graph)
relationmatcher = RelationshipMatcher(graph)
p = relationmatcher.match()
p = graph.run(
    "MATCH p=(a)-[r:`分子式`]->(b) where b.entity='e4095675' RETURN a")
'''

'''
./neo4j-import --into graph.db --nodes /home/xiaopeng/Desktop/AutoKnowledge/data/entity.csv --relationships /home/xiaopeng/Desktop/AutoKnowledge/data/relation.csv 
'''


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


print(hr2t("2", "nsjfs"))
print(ht2r("3", "chi"))
print(rt2h("4", "dwdhajk"))
print(h2r("5"))
print(t2r("6"))
