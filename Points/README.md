# Points Distance Calculator

This Python script calculates the distances between pairs of points and reads point coordinates from a file. The script defines a Points class to represent 2D points and includes methods to calculate distances and read points from a file.

#Class Points
#Method __init__(self, x, y)
Initializes a point object with x and y coordinates.
Method getDistance(self, other)
Calculates the Euclidean distance between two points using the formula: sqrt((other.x - self.x)^2 + (other.y - self.y)^2).
#Method readPointFile(fileName)
Reads point coordinates from a file.
Skips the first line of the file.
Parses the coordinates and creates Points objects.
Returns a list of Points objects.

# Usage
Create a text file named points.txt containing point coordinates in the format x,y (e.g., 1.0, 2.0).
Copy and paste the provided code into a Python file (e.g., points_distance_calculator.py).
Run the script using your preferred Python interpreter.
