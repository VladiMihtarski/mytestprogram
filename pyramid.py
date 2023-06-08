import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Изчисляване на обема на пирамидата
a = 0.5  # дължина на страната на квадрата
h = 1  # височина на пирамидата
V = (1/3) * a**2 * h
print(f"Обем на пирамидата: {V:.2f}")

# Изобразяване на пирамидата
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Върховете на квадрата
vertices = np.array([[0, 0, 0], [a, 0, 0], [a, a, 0], [0, a, 0]])
# Връх на пирамидата
apex = np.array([a/2, a/2, h])
# Списък със страните на квадрата и страната от върха до всеки връх на квадрата
faces = [[vertices[0], vertices[1], apex], [vertices[1], vertices[2], apex],
         [vertices[2], vertices[3], apex], [vertices[3], vertices[0], apex],
         [vertices[0], vertices[1], vertices[2], vertices[3]]]

# Изобразяване на страните на пирамидата
poly3d = Poly3DCollection(faces, alpha=.25, facecolor='r')
ax.add_collection3d(poly3d)

# Отметки на осите
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
