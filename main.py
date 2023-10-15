class Player:
    def __init__(self):
        self.player = "X"

    def changePlayer(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"

class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.symbol = Player()

    def mark(self, number):
        self.board[number - 1] = self.symbol.player

    def boardValid(self):
        if "-" in self.board:
            return False

    def moveValid(self):
        pass

    def win(self):
        pass

    def __str__(self):
        return self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' | \n' + \
               self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' | \n' + \
               self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' | '


if __name__ == "__main__":
    board = Board()

while(True):
    playersInput = int(input("Gebe die Nummer ein: "))
    board.mark(playersInput)

    print(board)

    board.symbol.changePlayer()






