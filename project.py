import math

def euclideanDistance(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def getMin(liste):
    min = liste[0]
    for i in range(len(liste)):
        if liste[i] < min:
            min = liste[i]
    return min


points = [(1, 2), (1, 3), (5, 6), (7, 8), (9, 10)]
point1 = points[0]
point2 = points[1]
point3 = points[2]
size = len(points)

distances = []
for i in range(0,size - 1):
    distances.append(euclideanDistance(points[i],points[i+1]))
            
print("Distances are: ")
print(distances)
print("Minimum Distance is: ")
print(getMin(distances))