from star1 import *
from functools import reduce

def logic_solver(line : str):
    game_info = extract_game_info(line)
    min_cubes_needed = {"red" : 1, "green" : 1, "blue" : 1}
    for draw in game_info.draws:
        for color, number in draw.items():
            min_cubes_needed[color] = max(min_cubes_needed[color], number)
    return reduce(lambda x, y: x * y, min_cubes_needed.values())


def main():
    power_sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            if power := logic_solver(line.strip()):
                power_sum += power
    print(power_sum)