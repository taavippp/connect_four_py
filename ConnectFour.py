from Board import Board
from Player import Player

class ConnectFour:
    width: int
    height: int
    board: Board

    def __init__(self, width: int, height: int, player: Player) -> None:
        self.width = width
        self.height = height
        self.board = Board(width, height, player).create_empty()
    
    def get_next_possible_boards(self, board: Board) -> list[Board]:
        boards: list[Board] = []
        for col_n in range(self.width):
            copy = Board(self.width, self.height, board.player).create_from(board.cells)
            column: list[Player] = copy.get_column(col_n)
            row_n: int = column.count(Player.NONE) - 1
            if (row_n == -1):
                continue
            copy.cells[(row_n * self.width) + col_n] = copy.player
            copy.player = Player.HUMAN if (copy.player == Player.COMPUTER) else Player.COMPUTER
            boards.append(copy)
        return boards

    def get_board_rating(self, board: Board, depth: int) -> int:
        next_boards: list[Board] = self.get_next_possible_boards(board)
        if (len(next_boards) == 0):
            return 0
        is_human_player: bool = (board.player == Player.HUMAN)
        if (board.is_won()):
            return 1 if (is_human_player) else -1
        elif (depth == 5):
            return 0
        ratings: list[int] = [self.get_board_rating(next_board, depth + 1) for next_board in next_boards]
        return min(ratings) if (is_human_player) else max(ratings)
    
    def get_best_move(self, board: Board) -> Board:
        next_boards: list[Board] = self.get_next_possible_boards(board)
        ratings: list[int] = [self.get_board_rating(next_board, 1) for next_board in next_boards]
        best_rating: int = self.get_board_rating(board, 1)
        return next_boards[ratings.index(best_rating)]

game: ConnectFour = ConnectFour(7, 6, Player.HUMAN)
game_has_winner: bool = False
for __i__ in range(game.width * game.height):
    print("\nCurrent:\n{0}".format(game.board), end = "\n\n")
    print("- - -- - -- - -- - -- - -\n")
    if (game.board.is_won()):
        game_has_winner = True
        break
    if (game.board.player == Player.HUMAN):
        boards: list[Board] = game.get_next_possible_boards(game.board)
        game.board = boards[int(input("Pick a free column (0 - {0}): ".format(len(boards) - 1)))]
    else:
        print("Computer is thinking..")
        game.board = game.get_best_move(game.board)

if (game_has_winner):
    print("Won by {}!".format(Player.HUMAN.name if (game.board.player == Player.COMPUTER) else Player.COMPUTER.name))
else:
    print("Nobody won.")