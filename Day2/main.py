num_safe = 0
lines = []

with open('input.txt') as f:
    line = f.readline()
    while line:
        lines.append(line)
        line = f.readline()


def is_line_valid(line: list[int]) -> bool:
    safe = True

    if not ((sorted(line) == line) or (sorted(line, reverse=True) == line)):
        safe = False

    for i in range(len(line) - 1):
        diff = abs(line[i] - line[i + 1])

        if (diff < 1) or (diff > 3):
            safe = False

    return safe


for line in lines:
    split_line = list(map(int, line.split()))

    if is_line_valid(split_line):
        num_safe += 1
    else:
        for i in range(len(split_line)):
            allow_one = split_line[:i] + split_line[i+1:]

            if is_line_valid(allow_one):
                num_safe += 1
                break

print(num_safe)


