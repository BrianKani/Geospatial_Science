import math

"""In this method, double loop is used to calculate the distances between each 
pair of four points (p0, p1, p2, p3)
"""
class Point():
    def __init__(self ,x ,y):
        self.x = x
        self.y = y

    def getDistance(self, other): #declaring method 
        return math.sqrt((other.x - self.x)**2 + (other.y-self.y)**2)
    
#declare three points
p1, p2, p3 = Point(1,5), Point(2,8), Point(10,3)

"""calculate distance and store as a list"""
dist1 = p1.getDistance(p2)
dist2 = p1.getDistance(p3)
dist3 = p2.getDistance(p3)

distances = [dist1,dist2,dist3]

# print(distance)
biggestDistance = 0.0
for i in range(len(distances)):
    currentDistance = distances[i]
    if currentDistance > biggestDistance:
        biggestDistance = currentDistance

print ("biggest distance is -> ",biggestDistance)





