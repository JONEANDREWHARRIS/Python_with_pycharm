class house:

    def __init__(self,door,rooms):
        self.door = door
        self.rooms = rooms

    def plan(self):
        print(self.rooms,self.door)

    def plugs(self):
        for item in range(self.rooms):
            print(4)
g = house(4,5)
g1 =g.plan()
g3= g.plugs()
# print(g)

