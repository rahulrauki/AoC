total = 0

def get_number1(line):
    start_num = end_num = 0
    for i in range(0, len(line), 1):
        if ord(line[i]) < 58:
            start_num = int(line[i])
            break
    for i in range(len(line) - 1, -1, -1):
        if ord(line[i]) < 58: 
            end_num = int(line[i])
            break
    return start_num * 10 + end_num

with open("input1.txt", "r") as f:
    for line in f:
        total += get_number1(line.strip())

print(total)