def find_all_paths(labyrinth):
    rows, cols = len(labyrinth), len(labyrinth[0])
    visited = [[False]*cols for _ in range(rows)]
    directions = [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]

    def is_valid(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return False
        if visited[x][y] or labyrinth[x][y] == '*':
            return False
        return True

    def dfs(x, y, path):
        if labyrinth[x][y] == 'e':
            print(path)
            return
        visited[x][y] = True
        for dx, dy, direction in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                dfs(new_x, new_y, path + direction)
        visited[x][y] = False

    dfs(0, 0, '')

# Въвеждане на брой редове и колони от конзолата
rows = int(input("Въведете брой редове: "))
cols = int(input("Въведете брой колони: "))

# Въвеждане на лабиринта от конзолата
labyrinth = []
for _ in range(rows):
    row = list(input("Въведете ред от лабиринта: "))
    labyrinth.append(row)

# Извикване на функцията за намиране на всички пътища
find_all_paths(labyrinth)
