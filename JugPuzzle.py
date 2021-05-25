class Jug:

    def __init__(self, water, capacity):
        self.water = water
        self.capacity = capacity

    def __str__(self):
        return f"({self.water}/{self.capacity})"


class Puzzle:
    high_score = 999999
    low_score = 0

    def __init__(self):
        self.moves = 0
        self.jugs = [Jug(8, 8), Jug(0, 5), Jug(0, 3)]
    
    
    def __str__(self):
        return f"{self.moves}\t0:{self.jugs[0]}\t1:{self.jugs[1]}\t2:{self.jugs[2]}"

    # Main function where game is played
    def play(self):
        while not self.is_game_won():
            print(self)
            self.get_move()
            self.moves += 1
        
        print(f"\nCongrats you won in {self.moves} moves!!!")
        self.set_score()
        self.play_again()

    # Checks if game is won
    def is_game_won(self):
        return self.jugs[0].water == 4 and self.jugs[1].water == 4

    # Takes input and calls transfer water
    def get_move(self):
        jugFrom = int(input("Spill from jug: "))
        jugTo = int(input("into jug: "))

        self.transfer_water(self.jugs[jugFrom], self.jugs[jugTo])

    # Transfers water between jugs
    def transfer_water(self, jugFrom, jugTo):
        if jugFrom.water > jugTo.capacity - jugTo.water:
            jugFrom.water -= (jugTo.capacity - jugTo.water)
            jugTo.water = jugTo.capacity
        else:
            jugTo.water += jugFrom.water
            jugFrom.water = 0

    # Asks to play again, resets instance if yes and starts new game
    def play_again(self):
        if(input("\nDo you want to play again?\ny/n - ") == "y"):
            print()
            self.__init__()
            self.play()

    # sets the high score and low score
    def set_score(self):
        if self.moves > Puzzle.low_score:
            Puzzle.low_score = self.moves

        if Puzzle.high_score > self.moves:
            Puzzle.high_score = self.moves

        print(f"Highest score: {Puzzle.high_score} moves")
        print(f"Lowest score: {Puzzle.low_score} moves")


Puzzle().play()
