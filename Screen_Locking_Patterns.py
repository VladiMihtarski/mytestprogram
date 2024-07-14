GRID_SIZE = 3
NUM_POINTS = GRID_SIZE * GRID_SIZE

def get_index(point):
    return ord(point) - ord('A')

def is_valid_move(from_idx, to_idx, visited, skip):
    if visited[to_idx]:
        return False
    if skip[from_idx][to_idx] != -1 and not visited[skip[from_idx][to_idx]]:
        return False
    return True

def dfs(current, remaining_length, visited, skip):
    if remaining_length == 0:
        return 1

    visited[current] = True
    count = 0

    for i in range(NUM_POINTS):
        if is_valid_move(current, i, visited, skip):
            count += dfs(i, remaining_length - 1, visited, skip)

    visited[current] = False
    return count

def count_patterns_from(first_point, length):
    if length <= 0 or length > NUM_POINTS:
        return 0

    skip = [[-1] * NUM_POINTS for _ in range(NUM_POINTS)]

    skip[get_index('A')][get_index('C')] = skip[get_index('C')][get_index('A')] = get_index('B')
    skip[get_index('A')][get_index('I')] = skip[get_index('I')][get_index('A')] = get_index('E')
    skip[get_index('A')][get_index('G')] = skip[get_index('G')][get_index('A')] = get_index('D')
    skip[get_index('B')][get_index('H')] = skip[get_index('H')][get_index('B')] = get_index('E')
    skip[get_index('C')][get_index('I')] = skip[get_index('I')][get_index('C')] = get_index('F')
    skip[get_index('C')][get_index('G')] = skip[get_index('G')][get_index('C')] = get_index('E')
    skip[get_index('D')][get_index('F')] = skip[get_index('F')][get_index('D')] = get_index('E')
    skip[get_index('G')][get_index('I')] = skip[get_index('I')][get_index('G')] = get_index('H')

    visited = [False] * NUM_POINTS
    return dfs(get_index(first_point), length - 1, visited, skip)

# Testing the function
print(count_patterns_from('D', 3))  # Expected output: 37
