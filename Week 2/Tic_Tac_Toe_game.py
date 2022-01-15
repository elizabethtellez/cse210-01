# Assigment name: Tic_Tac_Toe_game.py
# Author: Elizabeth Tellez

import random


class game:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                number = i * 3
                row.append(j+1+number)
            self.board.append(row)

    def player_one(self):
        return random.randint(0, 1)

    def fix_spot(self, number, player):
        count_long = 0
        for row in self.board:
            count_short = 0
            for item in row:
                if self.board[count_long][count_short] == number:
                    self.board[count_long][count_short] = player
                count_short = count_short + 1
            count_long = count_long + 1

    def player_win(self, player):
        win = None

        n = len(self.board)

        # Checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # Checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def board_filled(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X' or self.board[i][j] == 'O':
                    count = count + 1
        if count == 9:
            return True
        return False

    def player_swap(self, player):
        return 'X' if player == 'O' else 'O'

    def print_board(self):
        row_count = 1
        for row in self.board:
            count = 0
            for item in row:
                if count != 0:
                    print('|', end=' ')
                print(item, end=" ")
                count = count + 1
            print()
            if row_count != 3:
                print('- + - + - ')
                row_count = row_count + 1

    def main(self):
        self.create_board()

        player = 'X' if self.player_one() == 1 else 'O'
        while True:
            self.print_board()

            # Taking user input
            number = int(
                input(f"\n{player}'s turn to choose a square (1-9): "))
            print()

            # Fixing the spot
            self.fix_spot(number, player)

            # Checking whether current player is won or not
            if self.player_win(player):
                print(f"Player {player} wins the game!")
                break

            # Checking whether the game is draw or not
            if self.board_filled():
                print("Match Draw!")
                break

            # Swapping player turn
            player = self.player_swap(player)
       # Printing final view of board
        print()
        self.print_board()


# Initializing the game
tic_tac_toe = game()
tic_tac_toe.main()
