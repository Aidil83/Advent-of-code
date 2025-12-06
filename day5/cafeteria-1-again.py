with open("input.txt") as f:
    block1, block2 = f.read().strip().split("\n\n")

ranges = block1.split("\n")
numbers = block2.split("\n")

# Parse ranges into integer tuples
freshRanges = [tuple(map(int, r.split("-"))) for r in ranges]

# Parse numbers into integers
nums = list(map(int, numbers))


def countFresh(freshRanges: list[str], nums: list[str]) -> int:
    count = 0

    for num in nums:
        for start, end in freshRanges:
            if start <= num <= end:
                count += 1
                break
    
    return count

print(countFresh(freshRanges, nums))