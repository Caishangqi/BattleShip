from Board import Board
from typing import *


class Attack(object):
    def __init__(self, row: int, col: int, maker: str) -> None:
        self.row = row
        self.col = col
        self.maker = maker

    def attack(self, the_board: "Board", the_player: List[List[str]]) -> None:
        if the_board.grid[self.row][self.col].isalpha() == True and the_board.grid[self.row][self.col]!="X" and the_board.grid[self.row][self.col]!="O":
            the_board.grid[self.row][self.col] = "X"
            for i in the_player:
                if (str(self.row)+str(self.col)) in i:
                    print(f"You hit {self.maker}'s {i[0]}!")
                    i.pop(i.index(str(self.row)+str(self.col)))
                    if len(i)==1:
                        print(f"You destroyed {self.maker}'s {i[0]}")
        else:
            the_board.grid[self.row][self.col] = "O"
            print("Miss")

