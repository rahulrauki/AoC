def extract_data(line) -> tuple[set[str], list[str]]:
    rhs = line.split(":")[1]
    numbers : list[str] = rhs.strip().split("|")
    win_set = set(numbers[0].strip().split(" "))
    avail_set = set(numbers[1].strip().split(" "))
    return (win_set, avail_set)

def logic_solver(line) -> int:
    win_set, avail_list = extract_data(line)
    matches_count = -1
    for number in avail_list: 
        if number in win_set and number != '': matches_count += 1
    return 2 ** matches_count if matches_count >= 0 else 0

def main() -> None:
    total_points = 0
    with open("input.txt", "r") as f:
        for line in f:
            total_points += logic_solver(line.strip())
    print(total_points)

if __name__ == "__main__":
    main()