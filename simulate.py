import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# disable the sidebars on the pybullet simulation
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
# Slow down the simulation by iterating 1000 times
for i in range(1000):
    p.stepSimulation()

    # Print the loop variable to get a sense of iteration time
    print("Loop iteration:", i)

    # Sleep for 1/60th of a second
    time.sleep(1/60)

p.disconnect()

