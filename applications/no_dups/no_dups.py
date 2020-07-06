def no_dups(s:str, max:int = 1000):
    storage = [False] * max
    first = True
    last_index = len(s) - 1
    output = ''
    word = ''
    hash = 14695981039346656037

    for i, x in enumerate(s):
        if x != ' ':
            word += x
            hash = hash * 1099511628211
            hash = hash ^ ord(x)
        if  x == ' ' or i == last_index:
            index = hash % max
            if not storage[index]:
                if not first:
                    output += ' '
                else:
                    first = not first
                output += word
                storage[index] = True
            word = ''
            hash = 14695981039346656037

    return output        


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))