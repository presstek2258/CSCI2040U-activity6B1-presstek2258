# this program plays titactoe vs the computer

import random
from time import sleep

# tictactoe game
# player 1 is human
# player 2 is the computer


class PlayerNotDefinedError(Exception):
    pass


class Game:

    def __init__(self) -> None:
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 0
        self.game_running = True
        self.winner = 0

    def check_winner(self, player):

        for i in range(0, 3):
            if (
                self.board[i * 3] == player
                and self.board[(i * 3) + 1] == player
                and self.board[(i * 3) + 2] == player
            ):  # horizontal check
                return True
            if (
                self.board[i] == player
                and self.board[i + 3] == player
                and self.board[i + 6] == player
            ):  # vertical check
                return True
        if (
            self.board[0] == player
            and self.board[4] == player
            and self.board[8] == player
        ):  # diagnol top left to bottom right check
            return True
        if (
            self.board[2] == player
            and self.board[4] == player
            and self.board[6] == player
        ):  # diagnol top right to bottom left check
            return True

        return False  # the player has not won

    def board_full(self):
        if 0 in self.board:
            return False
        else:
            return True

    def load_first_player(self):
        print("rolling to see who goes first...")
        # sleep for 2 seconds to mimic rolling the die
        sleep(2)

        if random.randrange(2) == 0:
            self.turn = 1  # player goes first
        else:
            self.turn = 2  # com goes first
        print(f"Player {self.turn} goes first")

    def display_board(self):
        for i in range(len(self.board) // 3):
            print(f"{self.board[i*3]} {self.board[(i*3)+1]} {self.board[(i*3)+2]}")

    def play_player(self):
        move = False
        while not move:
            try:
                x = int(input("Where would you like to play: ")) - 1
            except ValueError as err:
                print("\nthe input could not be converted to an integer\n")
                raise err

            if 0 <= x <= 8:
                if self.board[x] == 0:
                    self.board[x] = 1  # 1 is for human player
                    move = True
                else:
                    print("That spot is already taken by a player")
            else:
                print("The input must be a number between 1-9 (inclusive)")

    def play_com(self):
        print("player 2 went")

        # TODO: computers turn / player 2's turn
        # for now use random choice

        move_index = -1
        move_found = False

        # good first move:
        if self.board[4] == 0:
            move_index = 4
            move_found = True

        # TODO: continue coding computer tictactoe choices

        # the rest is random choice:

        while move_found == False:
            move_index = random.randrange(0, 9)
            if self.board[move_index] == 0:
                move_found = True

        self.board[move_index] = 2  # the computer always plays 2


def main():

    g = Game()
    g.load_first_player()

    while g.game_running:

        if (
            g.board_full() and g.winner == 0
        ):  # if board is full and there is no winner it is a draw
            g.game_running = False
            g.display_board()
            print("It is a Draw!")
            break

        elif (g.turn == 1) and g.winner == 0:
            g.display_board()
            g.play_player()
            g.turn = 2

        elif (g.turn == 2) and g.winner == 0:
            g.play_com()
            g.turn = 1

        else:
            raise PlayerNotDefinedError("The player turn wasn't 1 or 2")

        # find if there is a winner and change g.winner
        if g.check_winner(1) == True:
            g.winner = 1
        elif g.check_winner(2) == True:
            g.winner = 2

        if g.winner != 0:
            g.game_running = False
            g.display_board()
            print(f"Player: {g.winner} Wins!")


main()
