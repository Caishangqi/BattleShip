from typing import List, Dict, Iterable
from Board import Board
from Attack import Attack
from typing import *


class Ship(object):

    """
    use boat_cover_point to determine which boat is hit. traversing all cover point
    to find the ship name of the hit boat.

    If one player hit others boat, program should traverse  all ships_with_entities = [] with
    ship_with_entities.is_hitted(player's target enter) to return the Boat name.

    This method could be stupid:)
    """

    def __init__(self)->None:
        self.boat_cover_point = []

    def is_hitted(self, the_board: "Board", the_player: List[List[str]], player_name1: str, player_name2: str)->None:
        while True:
            user_Input = input(f"{player_name2}, enter the location you want to fire at in the form row, column: ")
            try:
                user_Input.split()
            except:
                print(f"{user_Input} is not a valid location.")
                print("Enter the firing location in the form row, column")
                continue
            line=user_Input.split()
            if len(line)!=2:
                print(f"{user_Input} is not a valid location.")
                print("Enter the firing location in the form row, column")
                continue
            row=line[0]
            col=line[1]
            row=row.strip(",")
            try:
                int(row)
            except:
                print(f"Row should be an integer. {row} is NOT an integer.")
                continue
            try:
                int(col)
            except:
                print(f"Column should be an integer. {col} is NOT an integer.")
                continue
            if the_board.is_in_bounds(int(row), int(col)) == False:
                continue
            else:
                if the_board.grid[int(row)][int(col)] == "X" or the_board.grid[int(row)][int(col)] == "O":
                    print(f"You have already fired at {row}, {col}.")
                    continue
                else:
                    Attack(int(row), int(col), player_name1).attack(the_board, the_player)
                    break

    def board_copy(self, copy: List[List[str]])->None:
        for i in copy:
            for j in range(len(i)):
                if i[j].isalpha()==True and i[j] != "X" and i[j] != "O":
                    i[j]="*"
