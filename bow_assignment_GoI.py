import re

def read_file(fname):
    with open(fname, 'rb') as f:
        txt = f.read().decode('Windows-1252')
    return txt

def get_words(txt):
    txt = re.sub(r"\s+", " ", txt)
    txt = txt.split(" ")
    return txt

file = get_words(read_file("GoI.txt"))

def freq(txt):
    d = {}
    for word in txt:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

dict = freq(file)

sorted_dict = {}
sorted_keys = sorted(dict, key=dict.get, reverse=False)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict[w]
for key, value in sorted_dict.items():
    print(key, value)
