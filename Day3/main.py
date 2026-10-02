from time import perf_counter

def max_joltage(bank: str, k: int) -> int:
    start = 0
    end = len(bank) - k + 1
    result = []
    for _ in range(k):
        for digit in "9876543210":
            pos = bank.find(digit, start, end)
            if pos != -1:
                result.append(digit)
                start = pos + 1
                break
        end += 1
    return int("".join(result))
def main():
    with open("input.in") as f:
        banks = f.read().split()
    part1 = sum(max_joltage(bank, 2) for bank in banks)
    part2 = sum(max_joltage(bank, 12) for bank in banks)
    print("Part 1 solution:", part1)
    print("Part 2 solution:", part2)
    
if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"Total runtime: {perf_counter() - start_time:.6f} seconds")
