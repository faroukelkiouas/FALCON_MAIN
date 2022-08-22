import tinyik
import numpy as np

Falcon = tinyik.Actuator(
    [
        "z",
        [0.0, 0.0, 0.25],
        "y",
        [12, 0.0, 0.0],
        "y",
        [9.05, 0.0, 0.0],
        "x",
        [3.23, 0.0, 0.0],
        "y",
        [4.15, 0.0, 0.0],
    ]
)

# Since the joint angles are zero by default
print(Falcon.angles)

# Sets a position of the end-effector to calculate the joint angles:
Falcon.ee = [10 , 10 , 90]
#print(Falcon.angles)
Falcon.angles = np.round(np.rad2deg(Falcon.angles))
print(Falcon.angles)
x=-0
print(Falcon.angles[0]-x)
print(Falcon.angles[1]-x)
print(Falcon.angles[2]-x)
print(Falcon.angles[3]-x)
print(Falcon.angles[4]-x)

#tinyik.visualize(Falcon, target=[2.8, 0, 0.2])

