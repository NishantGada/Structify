# Chord Intersection Checker

## Overview

This Python script calculates and checks the intersection points between two chords represented by pairs of coordinates. The program determines whether the chords intersect and prints the results, including the count of intersections that occur inside the given circle.

## Usage

### Running the Script

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python intersection.py
   ```

4. The script will output information about the intersections, including whether the lines are parallel, the coordinates of the intersection points, and the total count of intersections inside the circle.

## Code Structure

A Python class named `Intersection` has been developed, which carries the logic for converting coordinates, calculating slopes, checking for intersections, and maintaining the intersection count. The main section creates an instance of the class and calls the necessary methods.

## Input

The script accepts input in the form of radian values and point labels. The example input provided is:

```python
Intersection([(0.78, 1.47, 1.77, 3.92), ("s1", "s2", "e1", "e2")])
```

We can add further inputs and more scenarios for further testing. 

## Output

The code outputs information about the intersections, including whether the lines are parallel, the coordinates of the intersection points, and the total count of intersections inside the circle.

## Performance

The code measures the execution time using the `process_time` function from the `time` module and prints the time taken to compute all intersections.