def parse_input(lines):
    ranges = []
    numbers = []
    i = 0
    n = len(lines)

    # Parse first block (ranges)
    while i < n and lines[i] != "":
        left, right = lines[i].split("-")
        ranges.append((int(left), int(right)))
        i += 1

    # Skip blank line(s)
    while i < n and lines[i] == "":
        i += 1

    # Parse second block (numbers)
    while i < n:
        numbers.append(int(lines[i]))
        i += 1

    return ranges, numbers

def read_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


lines = read_file("input.txt")
ranges, nums = parse_input(lines)



def countFresh(freshRanges, nums):
    freshLookup = set()

    for start, end in freshRanges:
        for x in range(start, end + 1):
            freshLookup.add(x)

    count = 0
    for num in nums:
        if num in freshLookup:
            count += 1

    return count

inputEx = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

# ranges, nums = parse_input(inputEx)
input = read_file('input.txt')

ranges, nums = parse_input(input)
# print(countFresh(ranges, nums))