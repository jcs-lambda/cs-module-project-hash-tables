def no_dups(s:str):
    seen = set()
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
            if hash not in seen:
                if not first:
                    output += ' '
                else:
                    first = not first
                output += word
                seen.add(hash)
            word = ''
            hash = 14695981039346656037

    return output        


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))