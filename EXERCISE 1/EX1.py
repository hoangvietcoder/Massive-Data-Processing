import os

path = "FileEX1"
files = os.listdir(path)

content = ""
dic = dict()

for file in files:
    with open(path + "/" + file, "r") as f:
        for line in f:
            line = line.strip()
            words = line.split()
            for word in words:
                if word in dic:
                    dic[word] = dic[word] + 1
                else:
                    dic[word] = 1

with open("Output.txt", "w") as f:
    for key in list(dic.keys()):
        f.writelines(key + ": " + str(dic[key]) + "\n")
    f.close()
