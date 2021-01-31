from os.path import dirname, join, realpath
import random

current_dir = dirname(realpath(__file__))

# Read in all the words in one go
with open(join(current_dir, "input.txt")) as f:
    words = f.read().split()

can_be_followed_by = {}
start_words = []
stop_words = set()
starters = ''.join([f'"{chr(i)}' for i in range(ord('A'), ord('Z') + 1)])
stoppers = '."?"!"'

# Analyze which words can follow other words
for i in range(len(words) - 1):
    word = words[i]
    next = words[i + 1]
    if word not in can_be_followed_by:
        can_be_followed_by[word] = [next]
    else:
        can_be_followed_by[word].append(next)
    
    if word[0] in starters or word[:2] in starters:
        start_words.append(word)
    if word[-1] in stoppers or word[-2:] in stoppers:
        stop_words.add(word)

# Construct 5 random sentences
for _ in range(5):
    output = [random.choice(start_words)]
    while output[-1] in can_be_followed_by and output[-1] not in stop_words:
        output.append(random.choice(can_be_followed_by[output[-1]]))
    print(' '.join(output))

