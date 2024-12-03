left_nums = []
right_nums = []

dists = []

# input inputs
with open("input.txt") as f:
    line = f.readline()
    while line:
        left_nums.append(int(line.split()[0]))
        right_nums.append(int(line.split()[1]))
        line = f.readline()

while left_nums:
    min_left = min(left_nums)
    left_nums.remove(min_left)
    min_right = min(right_nums)
    right_nums.remove(min_right)

    if min_left > min_right:
        dists.append(min_left - min_right)
    else:
        dists.append(min_right - min_left)

print(sum(dists))


