class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


class Accumulator(SM):
    def __init__(self, initValue):
        self.startState = initValue

    def getNextValues(self, state, input):
        return state + input, state + input

c = Accumulator(100)
c.start()
print c.step(20)
print c.step(2)
a = Accumulator()
print a.transduce([100, -3, 4, -123, 10])
print a.state