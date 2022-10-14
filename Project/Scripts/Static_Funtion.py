import numpy

def Distance(myDot, otherDot):
    return (
        ((myDot[0] - otherDot[0]) ** 2) +
        ((myDot[1] - otherDot[1]) ** 2)
    ) ** 0.5  # fast sqrt