import math
from time import process_time

class Intersection:
    def __init__(self, points):
        self.points = points
        self.mydict = {}
        # co-ordinates dictionary
        self.coords = {}
        # maintaining the count of all intersections inside the circle
        self.count = 0

    # getting the co-ordinates based on the input points, using Trigonometry
    def convert_to_coords(self):
        for i in self.points[1]:
            self.mydict[i] = self.points[0][self.points[1].index(i)]

        for i in self.mydict:
            x, y = math.cos(self.mydict[i]), math.sin(self.mydict[i])
            self.coords[i] = x, y

    # calculating the slopes of both the chords using mathematical concepts of co-ordinate geometry
    # formula being used:
        # m (slope) = (y2 - y1) / (x2 - x1)
    def calculate_slopes(self):
        slope1 = (self.coords["s1"][1] - self.coords["e1"][1]) / (self.coords["s1"][0] - self.coords["e1"][0])
        slope2 = (self.coords["s2"][1] - self.coords["e2"][1]) / (self.coords["s2"][0] - self.coords["e2"][0])
        return slope1, slope2

    # after calculating the slopes, we check for the intersection and calculate its co-ordinates
    def check_intersection(self, slope1, slope2):
        if slope1 != slope2:
            print("Not Parallel, checking further.. ")

            # formula being used:
                # x = (b2 - b1) / (m1 - m2)
                # y = m1 (x - x1) + y1
            x_intersection = (slope1 * self.coords["s1"][0] - self.coords["s1"][1] - slope2 * self.coords["s2"][0] + self.coords["s2"][1]) / (slope1 - slope2)
            y_intersection = slope1 * (x_intersection - self.coords["s1"][0]) + self.coords["s1"][1]

            # checking whether the intersection takes place inside or outside the circle
            if all(
                min(self.coords[point][0], self.coords[point2][0]) <= x_intersection <= max(self.coords[point][0], self.coords[point2][0]) and
                min(self.coords[point][1], self.coords[point2][1]) <= y_intersection <= max(self.coords[point][1], self.coords[point2][1])
                for point, point2 in [("s1", "e1"), ("s2", "e2")]
            ):
                # incrementing the intersection count if it takes place inside the circle
                print("Lines Intersect at Point:", (x_intersection, y_intersection))
                self.count += 1
            else:
                print("Intersection point falls outside the circle")
                print("Intersection Co-ordinates:", (x_intersection, y_intersection))
        else:
            print("Parallel Lines, No Intersection")

    # printing the final count of intersections taking place inside the circle
    def print_intersection_count(self):
        print("Number of Intersections:", self.count)


if __name__ == "__main__":
    t1_start = process_time()

    # Creating an instance of Intersection with the following input
    intersection = Intersection([(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")])

    # Calling the necessary methods
    intersection.convert_to_coords()
    slope1, slope2 = intersection.calculate_slopes()
    intersection.check_intersection(slope1, slope2)
    intersection.print_intersection_count()

    # calculating the program runtime
    t1_stop = process_time()
    d = t1_stop - t1_start
    print("Computing all Intersections took:", d * 1000, "milliseconds")