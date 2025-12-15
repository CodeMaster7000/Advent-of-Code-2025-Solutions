from __future__ import annotations
from typing import List, Set, Dict, Tuple
def read_grid(path: str) -> Tuple[List[str], int, int, int]:
    lines = [line.rstrip("\n") for line in open(path, "r", encoding="utf-8")]
    if not lines:
        raise ValueError("Empty input.")
    w = max(len(r) for r in lines)
    grid = [r.ljust(w, ".") for r in lines]
    h = len(grid)
    sx = sy = -1
    for y, row in enumerate(grid):
        x = row.find("S")
        if x != -1:
            if sx != -1:
                raise ValueError("Multiple 'S' found.")
            sx, sy = x, y
    if sx == -1:
        raise ValueError("No 'S' found.")
    return grid, w, h, sx
def solve_part1(grid: List[str], w: int, h: int, sx: int) -> int:
    active: Set[int] = {sx}
    splits = 0
    for y in range(1, h):
        if not active:
            break
        row = grid[y]
        next_active: Set[int] = set()
        for x in active:
            if x < 0 or x >= w:
                continue
            if row[x] == "^":
                splits += 1
                next_active.add(x - 1)
                next_active.add(x + 1)
            else:
                next_active.add(x)
        active = next_active
    return splits
def solve_part2(grid: List[str], w: int, h: int, sx: int) -> int:
    ways: Dict[int, int] = {sx: 1}
    for y in range(1, h):
        if not ways:
            break
        row = grid[y]
        next_ways: Dict[int, int] = {}
        for x, cnt in ways.items():
            if x < 0 or x >= w:
                continue
            if row[x] == "^":
                for nx in (x - 1, x + 1):
                    next_ways[nx] = next_ways.get(nx, 0) + cnt
            else:
                next_ways[x] = next_ways.get(x, 0) + cnt
        ways = next_ways
    ways = {sx: 1}
    exited = 0
    for y in range(1, h):
        if not ways:
            break
        row = grid[y]
        next_ways = {}
        for x, cnt in ways.items():
            if x < 0 or x >= w:
                exited += cnt
                continue
            if row[x] == "^":
                for nx in (x - 1, x + 1):
                    next_ways[nx] = next_ways.get(nx, 0) + cnt
            else:
                next_ways[x] = next_ways.get(x, 0) + cnt
        ways = next_ways
    exited += sum(cnt for x, cnt in ways.items() if 0 <= x < w)
    exited += sum(cnt for x, cnt in ways.items() if x < 0 or x >= w)
    return exited
def main() -> None:
    grid, w, h, sx = read_grid("input.in")
    p1 = solve_part1(grid, w, h, sx)
    p2 = solve_part2(grid, w, h, sx)
    print("Part 1 solution:", p1)
    print("Part 2 solution:", p2)
if __name__ == "__main__":
    main()
