
class Game(object):
    def __init__(self):
        # Game board, an array of strings from '0' to '8'
        # ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.board = [str(i) for i in range(9)]

        # List of players in the game:
        # - 'x'
        # - 'o'
        self.players = ['x', 'o']

        # Currently active player, 'x' always starts first in this game
        self.turn = 'x'
        print('starting game')

    def move(self, cell):
        # Is the cell claimed by player 'x' or player 'o'?
        if self.board[cell] not in self.players:
            # Store the player's name in the cell
            self.board[cell] = self.turn
        else:
            # advanced: catch and handle this error
            raise Exception

    def check_board_full(self):
        for cell in self.board:
            if cell not in self.players:
                return False
        return True

    def check_rows(self):
        return False

    def check_columns(self):
        return False

    def check_win(self):
        # Implement this!

        return False

    def print_board(self):
        # Can modify this if you want
        print('|'.join(self.board[:3]))
        print('|'.join(self.board[3:6]))
        print('|'.join(self.board[6:9]))
        return

    def print_turn(self):
        print("it's {}'s turn".format(self.turn))

    def get_player_move(self):
        # advanced: handle bad inputs (this could be a while loop)
        self.print_turn()
        player_input = input('select cell to play: ')
        return int(player_input)

    def reset_board(self):
        self.board = [str(i) for i in range(9)]

    def switch_turn(self):
        # Implement this!
        return

    def play(self):
        print('playing game')
        self.reset_board()
        self.print_board()
        while True:
            player_move = self.get_player_move()
            self.move(player_move)
            self.print_board()

            if self.check_win():
                # Check if the game ended
                print('{current_turn} won the game!'.format(current_turn=self.turn))
                return
            elif self.check_board_full():
                # Check if there are no more moves left
                print('game over! no one won.')
                return
            else:
                # Switch to next player's turn
                self.switch_turn()

game = Game()
game.play()
