import tinyik
import numpy as np

leg = tinyik.Actuator(
    [
        "z",
        [0.0, 0.0, 0.2],
        "y",
        [1.0, 0.0, 0.0],
        "y",
        [1.2, 0.0, 0.0],
        "x",
        [0.4, 0.0, 0.0],
        "y",
        [0.2, 0.0, 0.0],
    ]
)

leg.angles = np.deg2rad([30, -100, 110, 10, 0])
# tinyik.visualize(leg)
# leg.angles = [0, 0, 0, 0, 0]  # or np.deg2rad([30, 60])
# print(leg.ee)
tinyik.visualize(leg, target=[2.8, 0, 0.2])
