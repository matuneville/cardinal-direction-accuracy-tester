import math

def calcDistance(coord_A, coord_B):
    return math.sqrt((coord_A[0] - coord_B[0])**2 + (coord_A[1] - coord_B[1])**2)   # this would be the hypotenuse


# I trace a vector from myCoords to horizontalLine (EAST) and to friendCoords to calculate the angle
# Linear algebra formula (let T be the angle in rads) T = arccos(AB*AC / |AB|*|AC|)
# In this case, AB = myCoords -> HorizLine ; AC = myCoords -> friendCoords

def calcAngle(myCoords, horizLine, friendCoords):
    myCoords_copy = (myCoords[0] - myCoords[0], myCoords[1] - myCoords[1])
    horizLine_copy = (horizLine[0] - myCoords[0], horizLine[1] - myCoords[1])
    friendCoords_copy = (friendCoords[0] - myCoords[0], friendCoords[1] - myCoords[1])
    
    product = (horizLine_copy[0]*friendCoords_copy[0] + horizLine_copy[1]*friendCoords_copy[1]) / (calcDistance(myCoords_copy, horizLine_copy) * calcDistance(myCoords_copy, friendCoords_copy))
    rads = math.acos(product)
    if friendCoords_copy[1] < myCoords_copy[1]:
        rads = 2*math.pi - rads
    return math.degrees(rads)


def cardinalPoint(angle):
    if   22.50 < angle <= 67.50:
        return ["NE",(math.pi / 4)]
    elif 67.50 < angle <= 112.5:
        return ["N",(math.pi / 2)]
    elif 112.5 < angle <= 157.5:
        return ["NO", (math.pi * (3/4))]
    elif 157.5 < angle <= 202.5:
        return ["O", (math.pi)]
    elif 202.5 < angle <= 247.5:
        return ["SO", (math.pi * (5/4))]
    elif 247.5 < angle <= 292.5:
        return ["S", (math.pi * (3/2))]
    elif 292.5 < angle <= 337.5:
        return ["SE", (math.pi * (7/4))]
    return ["E", (math.pi * 2)]

