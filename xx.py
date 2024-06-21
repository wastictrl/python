import math

# Noktaların tanımlanması
points = [(1, 2), (3, 5), (7, 8), (4, 1), (9, 3)]

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Mesafelerin hesaplanması ve minimum mesafenin bulunması
distances = []
n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

# Sonucu yazdırma
print(f"Points: {points}")
print(f"All distances: {distances}")
print(f"Minimum distance: {min_distance}")
