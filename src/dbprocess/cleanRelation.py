import os
import numpy as np
relationsDic = np.load(os.getcwd() + "/../data/relationDic.npy")
entityDic = dict()
for line in open(os.getcwd() + "/../data/entity.csv"):
    triple = line.strip().split(",")
    entityDic[triple[0]] = triple[1]
relationsSet = set()
for item in relationsDic:
    if int(item[1]) > 10:
        relationsSet.add(item[0])
relationFile = open(os.getcwd() + "/../data/relation1.csv", "w")
relationFile.write(":START_ID,:END_ID,:TYPE\n")
propFile = open(os.getcwd() + "/../data/prop1.txt", "w")
for line in open(os.getcwd() + "/../data/relation.csv"):
    triple = line.strip().split(",")
    if triple[2] in relationsSet:
        relationFile.write(line)
    else:
        propFile.write(entityDic[triple[0]]+"\t" +
                       triple[2]+"\t"+entityDic[triple[1]]+"\n")
relationFile.close()
propFile.close()
