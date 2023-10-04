from Player import Player

class Board:
    width: int
    height: int
    cells: list[Player]
    player: Player

    def __init__(self, width: int, height: int, player: Player) -> None:
        self.width = width
        self.height = height
        self.player = player

    def create_empty(self):
        self.cells = []
        for __i__ in range(self.width * self.height):
            self.cells.append(Player.NONE)
        return self
    
    def create_from(self, cells: list[Player]):
        self.cells = [cell for cell in cells]
        return self
    
    def get_row(self, n: int) -> list[Player]:
        start: int = n * self.width
        return self.cells[start : start + self.width : 1]

    def get_column(self, n: int) -> list[Player]:
        return self.cells[n : self.width * self.height : self.width]
    
    def is_row_won(self, n: int) -> bool:
        points = 0
        last_cell: Player = Player.NONE
        row: list[Player] = self.get_row(n)
        for cell in row:
            if (last_cell != cell or cell == Player.NONE):
                points = 0
            else:
                points += 1
            if (points == 3):
                return True
            last_cell = cell
        return False

    def is_column_won(self, n: int) -> bool:
        points = 0
        last_cell: Player = Player.NONE
        column: list[Player] = self.get_column(n)
        for cell in column:
            if (last_cell != cell or cell == Player.NONE):
                points = 0
            else:
                points += 1
            if (points == 3):
                return True
            last_cell = cell
        return False

    def is_won(self) -> bool:
        for col in range(self.width):
            if (self.is_column_won(col)):
                # print("Victory on column {0}".format(col))
                return True
        for row in range(self.height):
            if (self.is_row_won(row)):
                # print("Victory on row {0}".format(row))
                return True
        return False
    
    def __repr__(self) -> str:
        result: str = ""
        for n in range(self.height):
            row: list[Player] = self.get_row(n)
            result += " | ".join([cell.value for cell in row])
            result += "\n"
        result += "Next: {0}".format(self.player.name)
        return result