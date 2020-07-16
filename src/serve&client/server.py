import threading
import socket
from time import strftime, localtime
import json
import numpy as np
#############################
import os
from py2neo import Graph, Node, Relationship, NodeMatcher, PropertyDict
import time
import random


id2entityDic = dict()
entity2idDic = np.load("../../data/entity_id.npy",
                       allow_pickle=True).item()  # 测试,e12

for item in entity2idDic:
    id2entityDic[entity2idDic[item][1:]] = item

graph = Graph('http://localhost:7474', username='neo4j', password='123321')


def hr2t(entityID, relationType):
    return "MATCH p=(h)-[r:`"+relationType+"`]->(t) where id(h)="+entityID+" RETURN t.` name`"


def ht2r(entityID_h, entityID_t):
    return "MATCH p=(h)-[r]->(t) where id(h)="+entityID_h+" and id(t)="+entityID_t + " RETURN r"


def rt2h(entityID, relationType):
    return "MATCH p=(h)-[r:`"+relationType+"`]->(t) where id(t)="+entityID+" RETURN h.` name`"


def h2r(entityID):
    return "MATCH p=(h)-[r]->(t) where id(h)="+entityID+" RETURN r"


def t2r(entityID):
    return "MATCH p=(h)-[r]->(t) where id(t)="+entityID+" RETURN r"


def id2name(entityID):
    p = graph.run("match (n) where id(n) = "+entityID+" return n.` name`")
    for item in p:
        return item.values()[0]
# （）的{关系}是{尾实体}?


def findHead(entityID, count=1):
    print("start")
    print(entityID)
    relations = []
    p = graph.run(h2r(entityID))
    for reltion in p:
        relations.append(reltion.values()[0].__class__.__name__)
    selectRelation = relations[random.randint(0, len(relations)-1)]
    print(relations)
    print(selectRelation)
    tails = []
    p = graph.run(hr2t(entityID, selectRelation))
    for tail in p:
        tails.append(tail.values()[0])
    print(tails)
    selectTail = tails[random.randint(0, len(tails)-1)]
    # print(id2entityDic[entityID]+"的"+selectRelation+"是"+selectTail)
    option = ['a', 'b', 'c', 'd']
    option[0] = id2name(entityID)
    question = "（   ）的"+selectRelation+"是"+selectTail
    for i in range(1, 4):
        randID = str(random.randint(0, 30000))
        option[i] = id2name(randID)
    return [question, option], ['A']

# {头实体}的{关系}是()?单选 || {头实体}的{关系}有()?


def findTail(entityID):
    print("start")
    print(entityID)
    relations = []
    p = graph.run(h2r(entityID))
    for reltion in p:
        relations.append(reltion.values()[0].__class__.__name__)
    selectRelation = relations[random.randint(0, len(relations)-1)]
    print(relations)
    print(selectRelation)
    p = graph.run(hr2t(entityID, selectRelation))
    tails = set()
    for tail in p:
        tails.add(tail.values()[0])
    tails = list(tails)
    print(tails)
    flag = False
    if len(tails) > 1:
        flag = True
    count = random.randint(1, len(tails))
    if count > 4:
        count = 4
    if flag:
        question = id2name(entityID)+"的"+selectRelation+"有(   )"
    else:
        question = id2name(entityID)+"的"+selectRelation+"是(   )"
    option = ['a', 'b', 'c', 'd']
    answer = []
    tmpIDs = []
    for i in range(count):
        tmpID = random.randint(0, len(tails)-1)
        while tmpID in tmpIDs:
            tmpID = random.randint(0, len(tails)-1)
        selectTail = tails[tmpID]
        option[i] = selectTail
        answer.append(chr(ord('A')+i))
    for i in range(4-count):
        randID = str(random.randint(0, 30000))
        option[count+i] = id2name(randID)
    print(answer)
    return [question, option], answer


def get_question():
    while True:
        try:
            classID = random.randint(0, 1)
            entityID = str(random.randint(0, 30000))
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
professions = ['a', 'b', 'c']

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
