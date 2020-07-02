import threading
import socket
from time import strftime, localtime
import json

#############################
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
    return "MATCH p=(h)-[r:`"+relationType+"`]->(t) where h.entity=\""+entityID+"\" RETURN t"


def ht2r(entityID_h, entityID_t):
    return "MATCH p=(h)-[r]->(t) where h.entity=\""+entityID_h+"\" and t.entity=\""+entityID_t + "\" RETURN r"


def rt2h(entityID, relationType):
    return "MATCH p=(h)-[r:`"+relationType+"`]->(t) where t.entity=\""+entityID+"\" RETURN h"


def h2r(entityID):
    return "MATCH p=(h)-[r]->(t) where h.entity=\""+entityID+"\" RETURN r"


def t2r(entityID):
    return "MATCH p=(h)-[r]->(t) where t.entity=\""+entityID+"\" RETURN r"

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
    print(answer)
    return [question, option], answer


def get_question(entity=""):
    while True:
        try:
            classID = random.randint(0, 1)
            entityID = "e"+str(random.randint(0, 5000000))
            if classID:
                return findTail(entityID)
            else:
                return findHead(entityID)
        except:
            pass
##############################


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
'''
def tcp_recv(sock, addr):
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()),data.decode('utf-8'))
        #sock.send(('Server:%s'% input()).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

def tcp_send(sock):
    while True:
       
        msg = input()
        if msg == 'exit':
            exit
        #print('Client:%s'%data.decode('utf-8'))
        sock.send((' From server : %s'% msg).encode('utf-8'))

    print('Connection from %s:%s closed.' % addr)
'''
professions = ['aa', 'b', 'c']

'''
def get_question():
    title = '一下那个选项不是数字？'
    options = ['Q', '人类', '2', '6']
    answer = ['A', 'B']
    question = [title, options]
    return question, answer
'''


def evaluate(sock, addr, profession):
    finalScore = 0

    count = 1
    while count <= 10:

        question, answer = get_question()

        if count == 3:
            send_msg = ['question', '-1', question]
        else:
            send_msg = ['question', str(count), question]
        json_string = json.dumps(send_msg)
        sock.send(json_string.encode('utf-8'))

        answer_from_client = sock.recv(1024).decode('utf-8')
        answer_from_client = list(answer_from_client)
        #answer_from_client = answer_from_client[1:]
        print(answer_from_client)
        print(len(answer_from_client))

        for option in answer_from_client:
            if option not in answer:
                score = 0
                break
            elif len(answer_from_client) == len(answer):
                score = 10
            else:
                score = 5
        finalScore = finalScore + score
        print("finalscore %d" % finalScore)
        count = count + 1

    return finalScore


def handle(sock, addr):

    # sock.send(('您的什么？').encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    while data.decode('utf-8') not in professions:

        send_msg = json.dumps(['profession error', 'error：无法找到相关职业'])
        sock.send(send_msg.encode('utf-8'))
        data = sock.recv(1024)

    profession = data.decode('utf-8')

    send_msg = json.dumps(['profession ok', '1'])
    sock.send(send_msg.encode('utf-8'))
    send_msg = json.dumps(['confirm', '下面将要回答问题，是否继续'])
    sock.send(send_msg.encode('utf-8'))

    data = sock.recv(1024)
    print(data.decode('utf-8'))
    if data.decode('utf-8') == 'yes':

        score = evaluate(sock, addr, profession)

        if score >= 60:
            send_msg = json.dumps(['pass', '通过'])
            sock.send(send_msg.encode('utf-8'))
        else:
            send_msg = json.dumps(['fail', '还差一点，继续努力吧'])
            sock.send(send_msg.encode('utf-8'))


while True:
    sock, addr = s.accept()
    print('Accept new connection from %s:%s...' % addr)
    t = threading.Thread(target=handle, args=(sock, addr))
    t.start()
'''
while True:
    # 接受一个新连接:
    # 创建新线程来处理TCP连接:
    tcp_send(sock)
'''
