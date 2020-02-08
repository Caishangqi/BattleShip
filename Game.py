from typing import *
from Board import Board
from Player import Player
from Ship import Ship
import copy


class Game(object):
    def __init__(self, dimension: List[int], ships: List[Tuple[str, int]], blank_char: str = "*") -> None:
        self.dimension=dimension
        self.blank_char = blank_char
        # this dimension[0] is row number dimension[1] is col number.
        self.board0=Board(dimension[0], dimension[1], blank_char)
        self.board1=Board(dimension[0], dimension[1], blank_char)
        self.boards = [self.board0, self.board1]
        self.ships = ships
        # Board[0] is player 1's Board[1] is player 2's
        self._cur_player_turn = 0
        self.copy_display=Board(dimension[0], dimension[1], blank_char)

    def play(self) -> None:
        self.players = []
        for player_num in range(2):
            if player_num==0:
                self.player0 = Player(self.players)
                self.players.append(self.player0.name)
                print(f"{self.players[0]}'s Placement Board")
                print(self.boards[0])
                self.player0.place_ships(self.ships, self.players[0], self.boards[0])
            else:
                self.player1 = Player(self.players)
                self.players.append(self.player1.name)
                print(f"{self.players[1]}'s Placement Board")
                print(self.boards[1])
                self.player1.place_ships(self.ships, self.players[1], self.boards[1])
        self.players_list=[self.player0, self.player1]
        while not self.is_game_over():
            if self._cur_player_turn==0:
                print(f"{self.players[0]}'s Scanning Board")
                self.copy_display.grid = copy.deepcopy(self.boards[1].grid)
                Ship().board_copy(self.copy_display.grid)
                print(self.copy_display)
                print(f"{self.players[0]}'s Board")
                self.display_game_state()
                Ship().is_hitted(self.boards[1], self.players_list[1].ships.boat_cover_point, self.players[1], self.players[0])
                self.copy_display.grid = copy.deepcopy(self.boards[1].grid)
                Ship().board_copy(self.copy_display.grid)
                print(f"{self.players[0]}'s Scanning Board")
                Ship().board_copy(self.copy_display.grid)
                print(self.copy_display)
                print(f"{self.players[0]}'s Board")
                self.display_game_state()
            elif self._cur_player_turn==1:
                print(f"{self.players[1]}'s Scanning Board")
                self.copy_display.grid = copy.deepcopy(self.boards[0].grid)
                Ship().board_copy(self.copy_display.grid)
                print(self.copy_display)
                print(f"{self.players[1]}'s Board")
                self.display_game_state()
                Ship().is_hitted(self.boards[0], self.players_list[0].ships.boat_cover_point, self.players[0], self.players[1])
                self.copy_display.grid = copy.deepcopy(self.boards[0].grid)
                Ship().board_copy(self.copy_display.grid)
                Ship().board_copy(self.copy_display.grid)
                print(f"{self.players[1]}'s Scanning Board")
                Ship().board_copy(self.copy_display.grid)
                print(self.copy_display)
                print(f"{self.players[1]}'s Board")
                self.display_game_state()
            self.change_turn()
        self.display_the_winner()

    def display_game_state(self) -> None:
        print(self.boards[self._cur_player_turn])

    def is_game_over(self)->bool:
        return self.someone_won()

    def someone_won(self) -> bool:
        count=0
        for i in self.boards[self._cur_player_turn].grid:
            for j in i:
                if j.isalpha()==True and j != "X" and j != "O":
                        count+=1
                else:
                    pass
        if count==0:
            return True
        else:
            return False

    def change_turn(self) -> None:
        if self._cur_player_turn == 0:
            self._cur_player_turn = 1
        elif self._cur_player_turn == 1:
            self._cur_player_turn = 0

    @property
    def cur_player(self) -> str:
        self.change_turn()
        return self.players[self._cur_player_turn]

    def display_the_winner(self)->None:
        print(f'{self.cur_player} won the game!')
