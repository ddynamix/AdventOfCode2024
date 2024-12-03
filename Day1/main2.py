left_nums = []
right_nums = []

scores = []

# input inputs
with open("input.txt") as f:
    line = f.readline()
    while line:
        left_nums.append(int(line.split()[0]))
        right_nums.append(int(line.split()[1]))
        line = f.readline()

for num in left_nums:
    count = right_nums.count(num)
    scores.append(num * count)

print(sum(scores))


