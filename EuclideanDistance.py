

points=[
    (1,2),
    (2,8),
    (6,8),
    (7,24)
]

distances=[]

def euclideanDistance(point1,point2):
    return (((point2[0] - point1[0])**2) + ((point2[1] - point1[1])**2)) ** 0.5 

for a in range(len(points)):
    for b in range(a+1,len(points)):
        distance=euclideanDistance(points[a],points[b])
        distances.append(distance)

minimum_distance=min(distances)
print(f"Minimum Öklid Mesafesi : {minimum_distance}")


