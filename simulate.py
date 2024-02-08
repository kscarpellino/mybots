import pybullet as p

physicsClient = p.connect(p.GUI)

# Slow down the simulation by iterating 1000 times
for _ in range(1000):
    p.stepSimulation()

p.disconnect()

