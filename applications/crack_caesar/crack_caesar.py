# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

from os.path import dirname, join, realpath
import sys


most_to_least = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S',
    'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y',
    'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
]


def char_frequency(words:str, chars:[str] = most_to_least) -> [(str, int)]:
    frequency = {}
    for char in words:
        if char not in chars:
            continue
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    
    return sorted(list(frequency.items()), key=lambda x: x[1], reverse=True)


def crack_ceasar(words:str):
    freq = char_frequency(words)
    mapping = {freq[i][0]:most_to_least[i] for i in range(len(freq))}
    transposed = ''.join(map(lambda x: mapping[x] if x in mapping else x, words))
    print(transposed)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        filename = join(dirname(realpath(__file__)), 'ciphertext.txt')
    else:
        filename = sys.argv[1]
    
    with open(filename) as f:
        crack_ceasar(f.read())
