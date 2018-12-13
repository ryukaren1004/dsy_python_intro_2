import string
from collections import Counter, defaultdict

with open('example.txt') as f:
    raw_word_list = [word.lower().strip() for word in f.read().split()]
    fc = map(lambda x: x.translate(string.maketrans("",""), string.punctuation), raw_word_list)

word_dic = defaultdict(list)

for i, item in enumerate(fc):
    if i < len(fc) - 1:
        word_dic[item].append(i)

out = {key: dict(Counter([fc[value[v]+1] for v in xrange(len(value))])) for key, value in word_dic.items()}

with open('alice.txt') as f:
    fc = []
    for line in f:
        map(lambda x: fc.append(x.strip()), line.split())

word_dic = defaultdict(list)

for i in xrange(len(fc)-2):
        word_dic[(fc[i], fc[i+1])].append(fc[i+2])
