def read_grid(filename):
    lines = open(filename).read().rstrip("\n").splitlines()
    width = max(len(line) for line in lines)
    return [line.ljust(width) for line in lines]
def split_problems(grid):
    height = len(grid)
    width = len(grid[0])

    problems = []
    start = None
    for c in range(width):
        if any(grid[r][c] != " " for r in range(height)):
            if start is None:
                start = c
        else:
            if start is not None:
                problems.append((start, c))
                start = None
    if start is not None:
        problems.append((start, width))
    return problems
def solve_part1(grid, problems):
    total = 0
    for a, b in problems:
        block = [row[a:b] for row in grid]
        op = block[-1].strip()
        numbers = []
        for row in block[:-1]:
            value = "".join(ch for ch in row if ch.isdigit())
            if value:
                numbers.append(int(value))
        if op == "+":
            total += sum(numbers)
        else:
            prod = 1
            for n in numbers:
                prod *= n
            total += prod
    return total
def solve_part2(grid, problems):
    total = 0
    height = len(grid)
    for a, b in problems:
        block = [row[a:b] for row in grid]
        op = block[-1].strip()
        numbers = []
        for c in range(b - a):
            digits = []
            for r in range(height - 1):
                ch = block[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                numbers.append(int("".join(digits)))
        if op == "+":
            total += sum(numbers)
        else:
            prod = 1
            for n in numbers:
                prod *= n
            total += prod
    return total
def main():
    grid = read_grid("input.in")
    problems = split_problems(grid)
    part1 = solve_part1(grid, problems)
    part2 = solve_part2(grid, problems)
    print("Part 1 solution:", part1)
    print("Part 2 solution:", part2)
if __name__ == "__main__":
    main()
