import hashlib

index = dict()
line_number = 1

fd = open('out', 'r')

for line in fd:
    for word in line.rstrip("\n").split(" "):
        key = hashlib.md5(word.encode()).hexdigest()
        pages = index.get(key, list())
        pages.append(str(line_number))
        index[key] = pages

    line_number += 1

fd.close()


fd = open('index', 'w')
for key in sorted(index.keys()):
    fd.write(key + ":" + ",".join(index.get(key,list())) + "\n")

fd.close()



