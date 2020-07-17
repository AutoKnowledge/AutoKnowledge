import json
import os
entityDic = dict()
for line in open(os.getcwd() + "../../data/entity.csv"):
    triple = line.strip().split(",")
    entityDic[triple[1]] = triple[0]
propDic = dict(dict())
for line in open(os.getcwd() + "../../data/prop.txt"):
    triple = line.strip().split("\t")
    if len(triple) != 3:
        triple = line.strip().split(",")
    try:
        index = entityDic[triple[0]]
    except:
        print(triple[0])
    print(index)
    tmpDic = propDic.get(index, None)
    if tmpDic is None:
        propDic[index] = {triple[1]: triple[2]}
    else:
        tmpstr = propDic[index].get(triple[1], "")
        if tmpstr == "":
            propDic[index][triple[1]] = triple[2]
        else:
            propDic[index][triple[1]] = tmpstr+"<;>"+triple[2]
with open(os.getcwd() + "../../data/prop.json", 'w') as f:
    json.dump(propDic, f, ensure_ascii=False)
