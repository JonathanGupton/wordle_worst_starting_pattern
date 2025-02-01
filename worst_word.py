from collections import defaultdict
from pprint import pprint

with open("words.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]

word_parts = defaultdict(list)
for word in words:
    for i in range(len(word)):
        fragment = word[:i] + "_" + word[i+1:]
        word_parts[fragment].append(word)

worst_word_fragment = ""
worst_word_count = -10e7
for k, v in word_parts.items():
    if len(v) > worst_word_count:
        worst_word_fragment = k
        worst_word_count = len(v)

worst_words = sorted(word_parts[worst_word_fragment])

pprint(worst_word_fragment)
pprint(worst_word_count)
pprint(worst_words)