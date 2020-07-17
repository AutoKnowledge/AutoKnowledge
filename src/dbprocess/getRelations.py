import os
import numpy as np
'''
relationdic = dict()
relationfile = open(os.getcwd() + "/../data/relations.txt", "w")
for line in open(os.getcwd() + "/../data/relation.csv"):
    triple = line.strip().split(",")
    relationdic[triple[2]] = relationdic.get(triple[2], 0)+1
relationdic_sort = sorted(
    relationdic.items(), key=lambda x: x[1], reverse=True)
np.save(os.getcwd() + "/../data/relationDic.npy", relationdic_sort)
for relation in relationdic_sort:
    relationfile.write(relation[0]+"\n")
relationfile.close()
'''

relations = np.load(os.getcwd() + "../../data/relationDic.npy")
level = [1, 10, 100, 1000]
for i in level:
    count = 0
    for item in relations:
        if int(item[1]) > i:
            count += 1
    print(i, count/len(relations))
    print("\n")
# np.save('my_file.npy', dictionary)
# read_dictionary = np.load('my_file.npy').item()
