def simulate_nested_loops(n, current_loop=[]):
    if len(current_loop) == n:
        print(*current_loop)
        return

    for i in range(1, n + 1):
        simulate_nested_loops(n, current_loop + [i])


n = int(input("Въведете стойността на n: "))
simulate_nested_loops(n)
