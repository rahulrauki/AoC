import typing

def check_adjacent(line_num, start, end, matrix) -> int:
    symbol_count = actual_num = 0
    if line_num == 0:
        if start > 0: 
            if matrix[line_num][start - 1] != "." or matrix[line_num + 1][start - 1] != '.': symbol_count += 1
        if end < len(matrix[line_num]) - 1: 
            if matrix[line_num][end + 1] != "." or matrix[line_num + 1][end + 1] != '.': symbol_count += 1
        for i in range(start, end + 1):
            if matrix[line_num + 1][i] != '.': symbol_count += 1
    elif line_num == len(matrix) - 1:
        if start > 0: 
            if matrix[line_num][start - 1] != "." or matrix[line_num - 1][start - 1] != '.': symbol_count += 1
        if end < len(matrix[line_num]) - 1: 
            if matrix[line_num][end + 1] != "." or matrix[line_num - 1][end + 1] != '.': symbol_count += 1
        for i in range(start, end + 1):
            if matrix[line_num - 1][i] != '.': symbol_count += 1
    else:
        if start > 0: 
            if matrix[line_num][start - 1] != "." or matrix[line_num - 1][start - 1] != '.' or matrix[line_num + 1][start - 1] != '.': symbol_count += 1
        if end < len(matrix[line_num]) - 1: 
            if matrix[line_num][end + 1] != "." or matrix[line_num - 1][end + 1] != '.' or matrix[line_num + 1][end + 1] != '.': symbol_count += 1
        for i in range(start, end + 1):
            if matrix[line_num - 1][i] != '.' or matrix[line_num + 1][i] != '.': symbol_count += 1
    print(int(''.join([matrix[line_num][i] for i in range(start, end + 1)])))
    if symbol_count == 0: return 0
    else: return int(''.join([matrix[line_num][i] for i in range(start, end + 1)]))


def logic_solver(matrix : list[list[str]]) -> int:
    part_sum = line_num = 0
    num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    for line in matrix:
        start, line_sum = '.', 0
        for i in range(len(line)):
            if line[i] in num_set: start = i
            elif start != ".":
                line_sum += check_adjacent(line_num=line_num, start=start, end=i - 1, matrix=matrix)
                start = '.'
        if start != ".": line_sum += check_adjacent(line_num=line_num, start=start, end=len(line) - 1, matrix=matrix)
        line_num += 1
        part_sum += line_sum
    return part_sum 

def main() -> None:
    with open("input.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]
    print(logic_solver(matrix))


if __name__ == "__main__":
    main()