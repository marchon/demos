import sys
class GeneratorClass:
    def __init__(self):
        print type(self)
        pass
    def generator(self):
        print str(type(self)) + " " + self
        for i in range(10):
            yield i

gen = GeneratorClass()

#quit(gen)

sys.debug()
for g in gen.generator("Hello"):
    print float(g)