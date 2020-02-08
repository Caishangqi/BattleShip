from typing import *
from Board import Board
from Ship import Ship


class Player(object):
    def __init__(self, other_players: Iterable["Player"])->None:
        self.name = self.get_name_from_player(other_players)
        self.ships = Ship()

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([i for i in other_players])
        while True:
            name = input(f'Player {len(other_players)+1} please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'Someone is already using {name} for their name.')
                print("Please choose another name.")

    def place_ships(self, ships: List[Tuple[str, int]], player_name: str, play_board: "Board") -> None:
        for i in range(len(ships)):
            ship_coordinates = [ships[i][0]]
            while True:
                while True:
                    self.direction = input(f"{player_name} enter horizontal or vertical for the orientation of {ships[i][0]} which is {ships[i][1]} long: ")
                    if self.direction != "h" and self.direction != "v" and self.direction != "horizontal" and self.direction != "vertical":
                        continue
                    else:
                        break
                while True:
                    user_Input=input(f"{player_name}, enter the starting position for your {ships[i][0]} ship, which is {ships[i][1]} long, in the form row, column: ")
                    try:
                        user_Input.split()
                    except:
                        continue
                    line = user_Input.split()
                    if len(line) != 2:
                        continue
                    self.y=line[0]
                    self.x=line[1]
                    self.y = self.y.strip(",")
                    try:
                        int(self.y)
                    except:
                        continue
                    try:
                        int(self.x)
                        break
                    except:
                        continue
                if self.check_ship_valid(ships[i], play_board) == True:
                    if self.direction == "h" or self.direction == "horizontal":
                        for k in range(int(self.x), int(self.x) + ships[i][1]):
                            play_board.grid[int(self.y)][k] = ships[i][0][0]
                        for l in range(ships[i][1]):
                            ship_coordinates.append(self.y + str(int(self.x) + l))
                    elif self.direction == "v" or self.direction == "vertical":
                        for k in range(int(self.y), int(self.y) + ships[i][1]):
                            play_board.grid[k][int(self.x)] = ships[i][0][0]
                        for l in range(ships[i][1]):
                            ship_coordinates.append(str(int(self.y) + l) + self.x)
                    break
                else:
                    continue
            self.ships.boat_cover_point.append(ship_coordinates)
            print(f"{player_name}'s Placement Board")
            print(play_board)

    def orientation_overlapped(self, play_board: "Board") -> bool:
        if int(self.x) <= (len(play_board.grid[0]) - 1) and int(self.y) <= (len(play_board.grid) - 1):
            if play_board.grid[int(self.y)][int(self.x)] == "*":
                return False
            else:
                return True
        else:
            return True

    def ship_horizontal_valid(self, ship: Tuple[str, int], play_board: "Board") -> bool:
        count=0
        for hrz in range(ship[1]):
            if (int(self.x) + hrz) > (len(play_board.grid[0]) - 1):
                count+=1
            else:
                if play_board.grid[int(self.y)][int(self.x) + hrz] != "*":
                    count+=1
                else:
                    pass
        if count==0:
            return True
        else:
            return False

    def ship_vertical_valid(self, ship: Tuple[str, int], play_board: "Board") -> bool:
        count=0
        for vet in range(ship[1]):
            if (int(self.y) + vet) > (len(play_board.grid)-1):
                count+=1
            else:
                if play_board.grid[int(self.y)+vet][int(self.x)] != "*":
                    count+=1
                else:
                    pass
        if count==0:
            return True
        else:
            return False

    def check_ship_valid(self, ship: Tuple[str, int], play_board: "Board") -> bool:
        if self.orientation_overlapped(play_board) == False:
            if self.direction == "h":
                if self.ship_horizontal_valid(ship, play_board) == True:
                    return True
                else:
                    return False
            elif self.direction == "v":
                if self.ship_vertical_valid(ship, play_board) == True:
                    return True
                else:
                    return False
        else:
            return False
