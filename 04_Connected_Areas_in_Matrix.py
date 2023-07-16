def find_connected_areas(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    areas = []

    def explore_area(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 0
        if matrix[row][col] != "-" or visited[row][col]:
            return 0

        visited[row][col] = True
        size = 1
        size += explore_area(row - 1, col)  # explore up
        size += explore_area(row + 1, col)  # explore down
        size += explore_area(row, col - 1)  # explore left
        size += explore_area(row, col + 1)  # explore right
        return size

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "-" and not visited[row][col]:
                area_size = explore_area(row, col)
                areas.append((row, col, area_size))

    areas.sort(key=lambda x: (-x[2], x[0], x[1]))  # Sort areas by size, position

    return areas


# Пример на използване:
matrix_rows = int(input())
matrix_cols = int(input())
matrix = []
for _ in range(matrix_rows):
    row = input()
    matrix.append(row)

connected_areas = find_connected_areas(matrix)

print(f"Total areas found: {len(connected_areas)}")
for i, area in enumerate(connected_areas, 1):
    row, col, size = area
    print(f"Area #{i} at ({row}, {col}), size: {size}")
