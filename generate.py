import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# Parameters for the first block
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

# Send the first block
pyrosim.Send_Cube(name="Box0", pos=[x, y, z], size=[length, width, 
height])

# Number of blocks in the tower
num_blocks = 10

# Loop to generate the tower
for i in range(1, num_blocks):
    # Calculate position and size for the current block
    x = 0
    y = 0
    z += height * 0.9  # Move the block up by 90% of its height
    length *= 0.9  # Decrease length by 10%
    width *= 0.9  # Decrease width by 10%
    height *= 0.9  # Decrease height by 10%

    # Send the current block
    pyrosim.Send_Cube(name=f"Box{i}", pos=[x, y, z], size=[length, width, 
height])

pyrosim.End()

