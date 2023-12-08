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

def get_num_index(line):
    start_num = len(line) - 1
    end_num = 0
    for i in range(0, len(line), 1):
        if ord(line[i]) < 58:
            start_num = i
            break
    for i in range(len(line) - 1, -1, -1):
        if ord(line[i]) < 58: 
            end_num = i
            break
    return start_num, end_num, int(line[start_num]), int(line[end_num])

def get_number2(line):

    num_dict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    num_set = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
    num_start_idx, num_end_idx, num_start, num_end = get_num_index(line=line)
    word_start = word_end = 0
    word_idx_start = len(line) - 1
    word_idx_end = 0

    for i in range(0, len(line), 1):
        flag = False
        for window in [3, 4, 5]:
            if i + window < len(line):
                number_word = line[i : i + window]
                if number_word in num_set:
                    word_start, word_idx_start = num_dict[number_word], i
                    flag = True
                    break 
        if flag: break

    for i in range(len(line), -1, -1):
        flag = False
        for window in [3, 4, 5]:
            if i - window >= 0:
                number_word = line[i - window : i]
                if number_word in num_set:
                    word_end, word_idx_end = num_dict[number_word], i - window
                    flag = True
                    break 
        if flag: break
    tens = ones = 0            
    if num_start_idx < word_idx_start: tens = num_start
    else : tens = word_start
    if num_end_idx < word_idx_end: ones = word_end
    else : ones = num_end
    # print(tens, ones)
    return tens * 10 + ones

with open("input.txt", "r") as f:
    for line in f:
        total += get_number2(line.strip())

print(total)