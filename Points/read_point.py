import math

class Points(): ## define a point class
    def __init__(self, x, y): ## init method for point class
        self.x = x
        self.y = y

 ## Declare getDistance as method of Point
    def getDistance (self, other):
        return math.sqrt((other.x - self.x)**2 + 
        (other.y - self.y)**2)
    
def readPointFile(fileName):
        file = open(fileName, 'r')
        points,index = [],0    #declare empty list for keeping points, and index for line Num
        for line in file: ## Read each line iteratively
            index += 1
            if index == 1:
                continue # "Ignore the first line 'point\n'"

            coords = line.split(':')[1] # split the line and get the coordinate,e.g,1.0, 1.0 
            ## Get the point x, y value
            xCoord = coords.split(',')[0]
            yCoord = coords.split(',')[1]
            point = Points(float(xCoord),float(yCoord))
            points.append(point) 
        file.close() 
        return points
        
"""# Call the function for parsing the point file"""

points = readPointFile('points.txt')
print(points)
 # getting a readPoint not defined
# print (points)
length = len(points) # get the length of points list
for i in range(length):
    point = points[i]
    print(point.x, point.y) ##print the x, y value of each point




