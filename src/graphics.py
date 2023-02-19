import matplotlib.pyplot as plt

from functions import calcDistance, calcAngle, cardinalPoint

def plotFriendsMap(myCoords, ithFriendCoords, ithFriendApproxCoords):
    # add actual and approximate points of friends
    actual_X = list(map(lambda coord : coord[0], ithFriendCoords))
    actual_Y = list(map(lambda coord : coord[1], ithFriendCoords))

    approx_X = list(map(lambda coord : coord[0], ithFriendApproxCoords))
    approx_Y = list(map(lambda coord : coord[1], ithFriendApproxCoords))

    plt.scatter(myCoords[0], myCoords[1])
    plt.scatter(actual_X, actual_Y, c="darkblue")
    plt.scatter(approx_X, approx_Y, c= "green")

    # add arrows
    for i in range(len(ithFriendCoords)):
        plt.arrow(actual_X[i], actual_Y[i], approx_X[i]-actual_X[i], approx_Y[i]-actual_Y[i], head_width=0.3, head_length=0.1, fc='orange', ec='orange', linestyle = "--")
        difference = round(calcDistance(ithFriendCoords[i], ithFriendApproxCoords[i]), 1)
        plt.text(approx_X[i]+4, approx_Y[i]+4, str(difference), ha = "right", va = "center")

    # add x and y axis lines, and set axis limits and names
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    # add a grid and plot all
    plt.grid(True)
    plt.show()
