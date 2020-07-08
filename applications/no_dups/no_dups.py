class Spacer:
    """.get() method returns '' on first call, subsequent calls return ' '."""
    def __init__(self):
        self.get = self._blank
    
    def _blank(self) -> str:
        self.get = self._space
        return ''

    def _space(self) -> str:
        return ' '


def no_dups(s:str):
    seen = set()
    output = ''
    spacer = Spacer()

    for word in s.split():
        if word not in seen:
            output = spacer.get().join([output, word])
            seen.add(word)

    return output        


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))