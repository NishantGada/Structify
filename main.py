import math
from time import process_time 

t1_start = process_time()
input = [(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")]
# input = [(0.9, 1.3, 1.70, 2.92), ("s1", "e1", "s2", "e2")]

mydict = {}
coords = {}
count = 0

for i in input[1]:
    mydict[i] = input[0][input[1].index(i)]

for i in mydict:
    # generating x & y co-ordinates based on the radian values using Trigonometry
    x, y = math.cos(mydict[i]), math.sin(mydict[i])
    coords[i] = x, y

slope1 = (coords["s1"][1] - coords["e1"][1]) / (coords["s1"][0] - coords["e1"][0])
slope2 = (coords["s2"][1] - coords["e2"][1]) / (coords["s2"][0] - coords["e2"][0])

if slope1 != slope2:
    print("Not Parallel, checking further.. ")

    # Calculating the intersection point based on the following mathematical formula
    # x = (b2 - b1) / (m1 - m2)
    # and, y = m1 (x - x1) + y1
    x_intersection = (slope1 * coords["s1"][0] - coords["s1"][1] - slope2 * coords["s2"][0] + coords["s2"][1]) / (slope1 - slope2)
    y_intersection = slope1 * (x_intersection - coords["s1"][0]) + coords["s1"][1]

    # Checking if the intersection point lies within our required bounds
    if (
        min(coords["s1"][0], coords["e1"][0]) <= x_intersection <= max(coords["s1"][0], coords["e1"][0]) and
        min(coords["s1"][1], coords["e1"][1]) <= y_intersection <= max(coords["s1"][1], coords["e1"][1]) and
        min(coords["s2"][0], coords["e2"][0]) <= x_intersection <= max(coords["s2"][0], coords["e2"][0]) and
        min(coords["s2"][1], coords["e2"][1]) <= y_intersection <= max(coords["s2"][1], coords["e2"][1])
    ):
        print("Lines Intersect at Point: ", (x_intersection, y_intersection))
        count += 1
    else:
        print("Intersection point falls outside the circle")
        print("Intersection Co-ordinates: ", (x_intersection, y_intersection))
else:
    print("Parallel Lines, No Intersection")

print("Number of Intersections: ", count)

t1_stop = process_time()
d = t1_stop - t1_start
print("Computing all Intersections took:", d * 1000, " milliseconds")