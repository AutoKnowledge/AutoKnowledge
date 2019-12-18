import os
pureBaike = open(os.getcwd() + "/../data/pure_baike_triples.txt", 'w')
i = 0
for line0 in open(os.getcwd() + "/../data/baike_triples.txt"):
    line = line0.replace("<a>", "").strip()
    line = line.replace("</a>", "")
    line = line.replace("\"\"", "")
    line = line.replace("\\\"", "\"")
    triple = line.split('\t')
    if len(triple) != 3:
        print(triple)
        continue
    if triple[1] == "BaiduCARD":
        continue
    pureBaike.write(line+'\n')
    i += 1
    if not i % 10000:
        print(i)
pureBaike.close()
