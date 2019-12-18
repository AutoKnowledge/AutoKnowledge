import os
relationset = set()
relationfile = open(os.getcwd() + "/../data/relations.txt", "w")
for line in open(os.getcwd() + "/../data/pure_baike_triples.txt"):
    triple = line.strip().split()
    relationset.add(triple[1])

for relation in relationset:
    relationfile.write(relation+"\n")
relationfile.close()
