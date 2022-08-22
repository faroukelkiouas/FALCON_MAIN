import klampt
from klampt.model import ik
world = klampt.WorldModel()
world.loadElement("data/robots/planar3R.rob")

robot= world.robot(0)
link = robot.link(2)
print(robot.getConfig())

obj = ik.objective(link,local=[1,0,0],world=[1.5,0,1])
solver = ik.solver(obj)
solver.solve()

robot.getConfig()
print(solver.getResidual())
