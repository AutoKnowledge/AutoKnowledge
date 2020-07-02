#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os
import perceptron
from segment import nroute


def add_curr_dir(name):
    return os.path.join(os.path.dirname(__file__), name)


class Analyze(object):
    def __init__(self):

        self.kg_model = None

        self.seg_mmseg = None

        self.seg_nroute = nroute.Segment()

    def init(self):
        self.init_cws()
        self.init_pos()
        self.init_ner()

    def load_userdict(self, userdict):
        self.seg_nroute.load_userdict(userdict)

    def init_cws(self):
        self.seg_nroute.init()

    def init_pos(self):
        if self.pos_model is None:
            self.pos_model = perceptron.Perceptron(
                add_curr_dir('model/pos.model'))

    def init_ner(self):
        if self.ner_model is None:
            self.ner_model = perceptron.Perceptron(
                add_curr_dir('model/ner.model'))

    def init_kg(self):
        if self.kg_model is None:
            self.kg_model = perceptron.Perceptron(
                add_curr_dir('model/kg.model'))

    def seg(self, sentence):
        return self.seg_nroute.seg(sentence, mode="default")

    def knowledge(self, text):  # 传入的是文本
        self.init_kg()
        words = self.seg(text)
        labels = self.kg_model.predict(words)
        return self.lab2spo(words, labels)

    def lab2spo(self, words, epp_labels):
        subject_list = []  # 存放实体的列表
        object_list = []
        index = 0
        for word, ep in zip(words, epp_labels):
            if ep[0] == 'B' and ep[2:] == '实体':
                subject_list.append([word, ep[2:], index])
            elif (ep[0] == 'I' or ep[0] == 'E') and ep[2:] == '实体':
                if len(subject_list) == 0:
                    continue
                subject_list[len(subject_list)-1][0] += word

            if ep[0] == 'B' and ep[2:] != '实体':
                object_list.append([word, ep[2:], index])
            elif (ep[0] == 'I' or ep[0] == 'E') and ep[2:] != '实体':
                if len(object_list) == 0:
                    return []
                object_list[len(object_list)-1][0] += word

            index += 1

        spo_list = []
        if len(subject_list) == 0 or len(object_list) == 0:
            pass
        elif len(subject_list) == 1:
            entity = subject_list[0]
            for obj in object_list:
                predicate = obj[1][:-1]
                spo_list.append([entity[0], predicate, obj[0]])
        else:
            for obj in object_list:
                entity = []
                predicate = obj[1][:-1]
                direction = obj[1][-1]
                for sub in subject_list:
                    if direction == '+':
                        if sub[2] > obj[2]:
                            entity = sub
                            break
                    else:
                        if sub[2] < obj[2]:
                            entity = sub

                if entity == []:
                    continue

                spo_list.append([entity[0], predicate, obj[0]])

        return spo_list
