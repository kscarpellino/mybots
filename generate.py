import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0,0,0] , size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,0] , size=[1,1,1])
    pyrosim.Send_Cube(name="Leg", pos=[1.0,0,1.5], size=[1,1,1])
    # Add a joint to connect Leg to Torso
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position=[0,0,0])
    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()

