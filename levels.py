class Level:
    def __init__(self):
        self.blocks = []

    def __contains__(self, item):
        return self.blocks.__contains__(item)

    def add(self, item):
        self.blocks.append(item)


levels = []
__level1 = Level()
for i in range(20):
    __level1.add([200 + i * 20, 200])

for i in range(3):
    __level1.add([200, 200 - i * 20])

for i in range(3):
    __level1.add([600, 200 - i * 20])

for i in range(20):
    __level1.add([200 + i * 20, 400])

for i in range(3):
    __level1.add([200, 400 + i * 20])

for i in range(3):
    __level1.add([600, 400 + i * 20])


levels.append(Level())
levels.append(__level1)

__level2 = Level()

for i in range(10):
    __level2.add([80 + i * 20, 60])

for i in range(10):
    __level2.add([700 - i * 20, 60])

for i in range(10):
    __level2.add([80 + i * 20, 520])

for i in range(10):
    __level2.add([700 - i * 20, 520])

for i in range(7):
    __level2.add([80, 60 + i * 20])

for i in range(7):
    __level2.add([700, 60 + i * 20])

for i in range(7):
    __level2.add([80, 520 - i * 20])

for i in range(7):
    __level2.add([700, 520 - i * 20])

levels.append(__level2)
