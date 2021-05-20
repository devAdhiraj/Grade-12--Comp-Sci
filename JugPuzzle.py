class Jug:
    def __init__(self, water, capacity):
        self.water = water
        self.capacity = capacity

    
class Puzzle:
    def __init__(self):
        self.moves = 0
        self.jugs = [Jug(8, 8), Jug(0, 5), Jug(0, 3)]
    
    
    def play(self):
        while(self.jugs[0].water != 4 or self.jugs[1].water != 4):
            print(f"{self.moves} {self.print_helper(0)} {self.print_helper(1)} {self.print_helper(2)}")

            jugFrom = int(input("Spill from jug: "))
            jugTo = int(input("into jug: "))
            self.transfer_water(jugFrom, jugTo)

            self.moves += 1

        print(f"Conrats you won in {self.moves} moves!!!")
    

    def print_helper(self, jugNumber):
        return f"{jugNumber}: ({self.jugs[jugNumber].water}/{self.jugs[jugNumber].capacity})"


    def transfer_water(self, jugFrom, jugTo):
        jugFrom = self.jugs[jugFrom]
        jugTo = self.jugs[jugTo]

        if jugFrom.water > jugTo.capacity - jugTo.water:
            jugFrom.water -= (jugTo.capacity - jugTo.water)
            jugTo.water = jugTo.capacity
        else:
            jugTo.water += jugFrom.water
            jugFrom.water = 0


Puzzle().play()
