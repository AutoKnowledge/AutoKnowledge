from py2neo import Graph, Node, Relationship, data
import os
graph = Graph('http://localhost:7474', username='neo4j', password='123321')
graph.run("match (n) detach delete n")


def List2Graph(RelationList):
    for Relation in RelationList:
        graph.create(Relation)


currHead = None
currHeadName = ""
RelationList = []
# tx = graph.begin()
for line0 in open(os.getcwd() + "../../data/baike_triples.txt"):
    line = line0.replace("<a>", "").strip()
    line = line.replace("</a>", "")
    triple = line.split("\t")
    if triple[0] != currHead:
        List2Graph(RelationList)
        # if RelationList != []:
        # tx.create(data.Subgraph(RelationList))
        # tx.commit()
        currHeadName = triple[0]
        currHead = Node(name=currHeadName)
        RelationList = []
    if triple[1] == "BaiduCARD":
        currHead["BaiduCARD"] = triple[2]
        continue
    RelationList.append(Relationship(
        currHead, triple[1], Node(name=triple[2])))
    print(triple)
