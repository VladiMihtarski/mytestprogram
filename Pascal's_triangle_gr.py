import matplotlib.pyplot as plt
import math

# Въвеждане на височината на пирамидата
height = int(input("Въведете височината на пирамидата: "))

# Изчисляване на числата от Триъгълника на Паскал
pascal_triangle = []
for i in range(height):
    row = []
    for j in range(i+1):
        coefficient = math.comb(i, j)
        row.append(coefficient)
    pascal_triangle.append(row)

# Изобразяване на пирамидата
fig, ax = plt.subplots()

# Брой редове и колони на пирамидата
rows = height
cols = 2 * height - 1

# Изобразяване на квадратите и числата от Триъгълника на Паскал
for i in range(rows):
    for j in range(i+1):
        # Разстояние от центъра на пирамидата до текущата колона
        offset = (cols - (i+1)) / 2
        square = plt.Rectangle((j+offset, rows-i-1), 1, 1, fill=False, edgecolor='black')
        ax.add_patch(square)

        # Изобразяване на числата от Триъгълника на Паскал
        number = pascal_triangle[i][j]
        ax.text(j+offset+0.5, rows-i-1+0.5, str(number), ha='center', va='center')

# Отметки на осите
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Промяна на мащаба на осите
ax.set_xlim([-0.5, cols-0.5])
ax.set_ylim([-0.5, rows-0.5])

# Промяна на скалата на осите, за да се запази квадратния вид на квадратите
ax.set_aspect('equal')

plt.show()
