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

    def moveValid(self, number):
        if self.board[number - 1] == " ":
            return True
        else:
            return False

    def win(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != " " or \
                self.board[3] == self.board[4] == self.board[5] and self.board[3] != " " or \
                self.board[6] == self.board[7] == self.board[8] and self.board[6] != " " or \
                self.board[0] == self.board[3] == self.board[6] and self.board[0] != " " or \
                self.board[1] == self.board[4] == self.board[7] and self.board[1] != " " or \
                self.board[2] == self.board[5] == self.board[8] and self.board[2] != " " or \
                self.board[0] == self.board[4] == self.board[8] and self.board[0] != " " or \
                self.board[2] == self.board[4] == self.board[6] and self.board[2] != " ":

            print(f"Player {self.symbol.player} win!")
            return True

        elif " " not in self.board:
            # 5,1,8,2,3,7,4,6,9
            print("It's a draw")
            return True

    def __str__(self):
        return self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' | \n' + \
               self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' | \n' + \
               self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' | \n'


if __name__ == "__main__":
    board = Board()

while True:
    while True:
        playersInput = int(input("Gebe die Nummer ein: "))
        if not board.moveValid(playersInput):
            print("Invalid move. Try again.")
        else:
            break

    board.mark(playersInput)
    print(board)

    if board.win():
        break

    board.symbol.changePlayer()

