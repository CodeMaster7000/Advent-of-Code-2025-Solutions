def is_part1_invalid(n: int) -> bool:
    s = str(n)
    L = len(s)
    if L % 2 != 0:
        return False
    half = L // 2
    return s[:half] == s[half:]
def is_part2_invalid(n: int) -> bool:
    s = str(n)
    L = len(s)
    for k in range(1, L // 2 + 1):
        if L % k == 0:
            block = s[:k]
            if block * (L // k) == s:
                return True
    return False
def generate_repeated_numbers(max_digits: int):
    nums = set()
    for block_len in range(1, max_digits + 1):
        for repeats in range(2, max_digits // block_len + 1):
            total_len = block_len * repeats
            if total_len > max_digits:
                continue
            start = 10 ** (block_len - 1)
            end = 10 ** block_len
            for base in range(start, end):
                s = str(base) * repeats
                nums.add(int(s))
    return nums
def main():
    with open("input.in") as f:
        ranges = [
            tuple(map(int, part.split("-")))
            for part in f.read().strip().split(",")
        ]
    max_val = max(b for _, b in ranges)
    max_digits = len(str(max_val))
    repeated_nums = generate_repeated_numbers(max_digits)
    part1_sum = 0
    part2_sum = 0
    for lo, hi in ranges:
        for n in repeated_nums:
            if lo <= n <= hi:
                if is_part1_invalid(n):
                    part1_sum += n
                if is_part2_invalid(n):
                    part2_sum += n
    print("Part 1 solution:", part1_sum)
    print("Part 2 solution:", part2_sum)

if __name__ == "__main__":
    main()
