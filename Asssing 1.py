#   Title:  PA1 PID1:A98017967 PID2:A91085115
#   Name1:  Ze Dan Li,
#   PID1:   A98017967
#   Name2:  Yinji Lu
#   PID2:  A91085115

import random
import numpy
from graphics import *

# Generates an array based on the data
def test(times, percent, obsize):
    observations = [0] * obsize
    random.seed(10)

    for i in range(0,times):
        int1 = percent * obsize
        int2 = obsize
        for j in range (0, obsize):
            next = int1/int2
            rand = random.random()
            if rand < next:
                observations[j] += 1
                int1 = int1 - 1
            int2 = int2 - 1
    return observations
    
def cal_mean(observations):

def cal_stdv(observations):

# Calculates the mean and normalizes it based on the runs
def meancalc(obsize):
    mean = []
    runs = 1

    for i in range (5):
        runs = runs *10
        data = test(runs, 0.1, obsize)
        mean.append(numpy.mean(data)/runs)
    return mean

# Calculates the STD and normalizes it based on the runs
def stdcalc(obsize):
    mean = []
    runs = 1

    for i in range (5):
        runs = runs *10
        data = test(runs, 0.1, obsize)
        mean.append(numpy.std(data)/runs)

    return mean

# Main Function to plot the graph
# Scales the points in a 500x500 window then draws the line
# X-axis is the number of runs scaled to 500x500 window
# Y-axis is the mean scaled to 500x500 window
def plotgraph(runs, mean):
    win = GraphWin("Number of runs VS mean", 500, 500)
    points = []

    for i in range (5):
        c = Point((runs[i]/100000)*500 , 500-(mean[i]*500))
        points.append(c)
        c.draw(win)

    for i in range (len(points)-1):
        a = Line(points[i], points[i+1])
        a.draw(win)

    win.getMouse() # pause for click in window
    win.close()

# Reads the input data
with open('abalone.txt') as linetext:
    text = linetext.readlines()
lines = len(text)
print (lines)

<<<<<<< HEAD
mean = meancalc(lines)
std = stdcalc(lines)
runs = [10, 100, 1000, 10000, 100000]

print("Runs: " + str(runs))
print("Mean: " + str(mean))
print("STD: " + str(std))

plotgraph(runs, mean)
=======
print(test(10, 0.1, 100))
>>>>>>> origin/master
