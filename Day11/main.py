from functools import cache
from time import perf_counter
def parse_input(filename="input.in"):
    graph = {}
    with open(filename) as f:
        for line in f:
            if line.strip():
                node, targets = line.split(":")
                graph[node] = targets.split()
    return graph
def solve(graph):
    get_neighbours = graph.get
    def make_counter(target):
        @cache
        def count_paths(node):
            if node == target:
                return 1
            total = 0
            for neighbour in get_neighbours(node, ()):
                total += count_paths(neighbour)
            return total
        return count_paths
    to_out = make_counter("out")
    to_dac = make_counter("dac")
    to_fft = make_counter("fft")
    part1 = to_out("you")
    dac_to_fft = to_fft("dac")
    if dac_to_fft:
        part2 = (
            to_dac("svr")
            * dac_to_fft
            * to_out("fft")
        )
    else:
        fft_to_dac = to_dac("fft")
        part2 = (
            to_fft("svr") * fft_to_dac * to_out("dac")
            if fft_to_dac
            else 0
        )
    return part1, part2
def main():
    graph = parse_input()
    part1, part2 = solve(graph)
    print("Part 1 solution:", part1)
    print("Part 2 solution:", part2)
    
if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"Total runtime: {perf_counter() - start_time:.6f} seconds")
