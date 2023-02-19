import math, random

from functions import calcDistance, calcAngle, cardinalPoint
from graphics import plotFriendsMap

myCoords = (79,-71)
horizLine = (myCoords[0]+1, myCoords[1]) # used to calc the angle

# Each index has the same i-th friend data, then I fill the data
ithFriendCoords = []
ithFriendDistance = []
ithFriendAngle = []
ithFriendApproxCoords = []

# Generate 7 random values of X and Y
for i in range (7):
    x, y = random.uniform(-90.00, 90.000), random.uniform(-90.00, 90.00)
    ithFriendCoords.append((x,y))

for ithFriend in ithFriendCoords:
    # Fill distance array
    distFromTo = calcDistance(myCoords, ithFriend) 
    ithFriendDistance.append(distFromTo)

    # Fill angle inclination array
    angleFromTo = calcAngle(myCoords, horizLine, ithFriend)
    ithFriendAngle.append(angleFromTo)

    # Fill approximate coords array
    directionTo = cardinalPoint(angleFromTo)
    ithFriendApproxCoords.append((((math.cos(directionTo[1])) * distFromTo) + myCoords[0], ((math.sin(directionTo[1])) * distFromTo) + myCoords[1]))

plotFriendsMap(myCoords, ithFriendCoords, ithFriendApproxCoords)

print("Program finished")
