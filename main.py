### Proportional-Pursuit
### Jeffrey Hess

## Program Outline
## ---------------
## Generate random position and starting velocity for both objects
## Run simulation and record data for each step

## Algorithm Outline (Proportional Pursuit methodology)
## ---------------------------------------------------
## Option 1
## a(n) : acceleraton perpendicular to the pursuer instantaenous velocity vector
## N    : navigation contastant (3 < N < 5)
## L    : line of sight rate (time derivative of line of sight angle)
## V    : closing velocity

## Option 2


# Imports
import numpy as np
import matplotlib.pyplot as plt


# Global Variables
VELO_PURSER = 0
VELO_TARGET = 0
HEADING_PURSER = 0
HEADING_TARGET = 0
POS_PURSER = 0
POS_TARGET = 0
LOS_RATE = 0
ACCELERATION = 0

# Functions

def generate_starting_conditions():
    global VELO_PURSER, VELO_TARGET, HEADING_PURSER, HEADING_TARGET, POS_PURSER, POS_TARGET

    VELO_PURSER = np.array([[np.random.uniform(0, 100)], [np.random.uniform(0, 100)]])
    VELO_TARGET = np.array([[np.random.uniform(0, 100)], [np.random.uniform(0, 100)]])
    HEADING_PURSER = np.random.uniform(0, 360)
    HEADING_TARGET = np.random.uniform(0, 360)
    POS_PURSER = np.array([[0], [0]])
    POS_TARGET = np.array([[np.random.uniform(0, 100)], [np.random.uniform(0, 100)]])
    pass

def plot_position():
    global VELO_PURSER, VELO_TARGET, HEADING_PURSER, HEADING_TARGET

    # Define positions based on initial velocities and headings
    velocity_purser = VELO_PURSER.flatten()
    velocity_target = VELO_TARGET.flatten()

    position_purser = POS_PURSER.flatten()
    position_target = POS_TARGET.flatten()

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.quiver(
        position_purser[0], position_purser[1], velocity_purser[0], velocity_purser[1],
        angles='xy', scale_units='xy', scale=1, color='blue', label='Purser Velocity'
    )
    plt.quiver(
        position_target[0], position_target[1], velocity_target[0], velocity_target[1],
        angles='xy', scale_units='xy', scale=1, color='red', label='Target Velocity'
    )

    plt.xlim(-10, 490)
    plt.ylim(-10, 490)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Pursuer and Target Velocities")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()
    plt.show()
    pass

def calc_closing_velocity():
    pass

def calc_los_rate():
    pass

def calc_acceleration():
    pass

# Main Execution
if __name__ == "__main__":
    generate_starting_conditions()
    plot_position()
    pass




