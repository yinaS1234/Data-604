# Import libraries
import simpy
import random

# Function to simulate rolling a die
def roll_dice():
    return random.randint(1,6)


# Simulation function
def gameofchance(env,results):
    while True:
        outcome=roll_dice()
        results[outcome-1] += 1
        yield env.timeout(1)


# Initialize the simulation environment
env=simpy.Environment()
# List to keep track of die outcomes
results=[0,0,0,0,0,0]
# Add the process
env.process(gameofchance(env,results))
# Run the simulation
env.run(until=1000)

# Display the results
for i in range(6):
    print(f'Number {i+1}:{results[i]} times')

