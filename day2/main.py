from GameInfo import GameInfo
from typing import *

def extract_game_info(line : str) -> GameInfo:
    game_info = GameInfo()
    game_info.game_id = int(line.split(":")[0].split(" ")[1])
    draws_list = []
    for draw in line.split(":")[1].split(";"):
        draw_dict = dict()
        for cubes in draw.split(","):
            number, color = cubes.strip().split(" ")
            draw_dict[color] = int(number)
        draws_list.append(draw_dict)
    game_info.draws = draws_list
    return game_info

def logic_solver(line : str) -> int:
    given_info = {"red" : 12, "green" : 13, "blue" : 14}
    game_info = extract_game_info(line)
    id, draws = game_info.game_id, game_info.draws
    for draw in draws:
        for color, number in draw.items():
            if given_info[color] < number: return 0
    return id

def main():
    game_id_count = 0
    with open("input.txt", "r") as f:
        for line in f:
            if id := logic_solver(line.strip()):
                game_id_count += id
    print(game_id_count)

if __name__ == "__main__":
    main()