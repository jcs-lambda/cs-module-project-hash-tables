from os.path import dirname, join, realpath
import re, sys


ignore = re.compile(r'[]":;,.+=/\\|[{}()*^&-]')


def word_count(s):
    s = ignore.sub('', s.lower()).split()
    word_count = {}
    max_len = 0
    for w in s:
        if w not in word_count:
            word_count[w] = 1
        else:
            word_count[w] += 1
        if len(w) > max_len:
            max_len = len(w)

    return word_count, max_len


def histogram(words:str):
    word_counts, max_len = word_count(words)
    words = [(word, -count) for word, count in word_counts.items()]
    words.sort(key=lambda x: [x[1], x[0]])
    for word in words:
        print(f'{word[0]:{max_len+2}}{"#"*-word[1]}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        filename = join(dirname(realpath(__file__)), 'robin.txt')
    else:
        filename = sys.argv[1]
    
    with open(filename) as f:
        histogram(f.read())
