class PowerTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def next(self):
        if self.n < self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

#
# a = PowerTwo(10)
# print(type(a))
# pa = iter(a)
# print(dir(pa))
# print(type(pa))
# print(next(pa))

class powerTwo:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def next(self):
        if self.start <= self.end:
            result  = self.start ** 2
            self.start += 1
            return result
        else:
            raise StopIteration
a = PowerTwo(5)
i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))



class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = sentence.split()

    def __iter__(self):
        return self

    def next(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


words = Sentence("this is anil kumar")
for word in words:
    #print(word)
    pass

def senetence(sen):
    for word in sen.split():
        yield word
p = senetence("this is apathapa")
print(next(p))
print(next(p))
print(next(p))
