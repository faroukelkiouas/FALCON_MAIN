import tinyik
#pip install tinyik==2.2.1
#pip install open3d-python

arm = tinyik.Actuator(['z', [1., 0., 0.], 'z', [1., 0., 0.]])
import numpy as np

arm.angles = [np.pi / 6, np.pi / 3]  # or np.deg2rad([30, 60])
print(arm.ee)
arm.ee = [2 / np.sqrt(2), 2 / np.sqrt(2), 0.]
print(arm.angles)
#array([  7.85398147e-01,   3.23715739e-08])
np.round(np.rad2deg(arm.angles))
#array([ 45.,   0.]

leg = tinyik.Actuator([[.3, .0, .0], 'z', [.3, .0, .0], 'x', [.0, -.5, .0], 'x', [.0, -.5, .0]])
leg.angles = np.deg2rad([30, 45, -90])
tinyik.visualize(leg)