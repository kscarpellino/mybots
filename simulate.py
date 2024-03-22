import pybullet as p
import pybullet_data
import pyrosim
import time

# Connect to the physics server
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set up the simulation environment
p.setGravity(0, 0, -9.8)
# Load the robot from body.urdf into an object called robotId
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

# Prepare Pyrosim for simulation
pyrosim.Prepare_To_Simulate(0)

# Iterate through the simulation steps
for i in range(1000):
    # Step the simulation
    p.stepSimulation()
    # Get touch sensor value for the back leg
    # Note: You might need to adjust the link name "BackLeg" if it's incorrect
    backLegTouch = 1 if p.getContactPoints(bodyA=robotId, linkIndexA=2) else -1
    print(backLegTouch)
    # Print the loop iteration for monitoring
    print("Loop iteration:", i)
    # Sleep for a short duration to control simulation speed
    time.sleep(1 / 60)

# Disconnect from the physics server
p.disconnect()

