import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# Parameters for the first block
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

# Number of blocks in each tower
num_blocks = 10
# Number of towers
num_towers = 5

# Loop to generate towers
for tower_index in range(num_towers):
    # Reset dimensions for each tower
    current_length = length
    current_width = width
    current_height = height
    current_z = z
    
    # Send the first block for the current tower
    pyrosim.Send_Cube(name=f"Box{tower_index}_0", pos=[x, y, current_z], size=[current_length, current_width, current_height])

    # Loop to generate the tower
    for block_index in range(1, num_blocks):
        # Calculate position and size for the current block
        x = tower_index  # Adjust x position for each tower
        y = 0
        current_z += current_height * 0.9  # Move the block up by 90% of its height
        current_length *= 0.9  # Decrease length by 10%
        current_width *= 0.9  # Decrease width by 10%
        current_height *= 0.9  # Decrease height by 10%

        # Send the current block for the current tower
        pyrosim.Send_Cube(name=f"Box{tower_index}_{block_index}", pos=[x, y, current_z], size=[current_length, current_width, current_height])

pyrosim.End()

