import re

ignore = re.compile(r'[]":;,.+=/\\|[{}()*^&-]')

def word_count(s):
    s = ignore.sub('', s.lower()).split()
    word_count = {}
    for w in s:
        if w not in word_count:
            word_count[w] = 1
        else:
            word_count[w] += 1

    return word_count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))