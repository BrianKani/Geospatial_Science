# Geospatial Distance Calculator
This Python script calculates the distances between pairs of four points in a 2D space using the Euclidean distance formula. The script defines a Point class with methods to compute distances between points. The distances are calculated among three points, and the script identifies and prints the biggest distance among them.

# Methodology
The script employs a double loop to calculate the distances between each pair of points (p0, p1, p2, p3). The Point class initializes points with x and y coordinates. The getDistance method computes the Euclidean distance between two points using the mathematical formula √((x2 - x1)^2 + (y2 - y1)^2).

# Usage

Copy and paste the provided code into a Python file (e.g., geospatial_distance_calculator.py).
Run the script using your preferred Python interpreter.

# Code Explanation
Three points (p1, p2, p3) are declared with specific coordinates.
Distances between pairs of points are calculated and stored in a list (distances).
The script iterates through the list of distances and identifies the biggest distance.
The biggest distance is printed to the console.
