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

N = 3

# Functions

def generate_starting_conditions():
    
    # Initial Velocities
    velocity_pursuer = np.array([[12], [5]])
    velocity_target = np.array([[6], [2]])

    # Initial Positions
    position_pursuer = np.array([[0], [0]])
    position_target = np.array([[50], [100]])

    # Initial Acceleration
    acceleration = np.array([[0], [0]])

    return (velocity_pursuer, velocity_target, position_pursuer, position_target, acceleration)

def calculate_acceleration(velocity_pursuer, velocity_target, position_pursuer, position_target, los_angle, los_angle_old):

    # Calculate Target Velocity relative to pursuer
    relative_velocity_target = velocity_target - velocity_pursuer

    delta_los = (los_angle - los_angle_old) 

    # Calculate Acceleration
    acceleration = N * relative_velocity_target * delta_los

    print("ACCELERATION: x:%f y:%f" % (acceleration[0], acceleration[1]))

    return acceleration

def calculate_los(velocity_pursuer, position_pursuer, position_target):

    # Calculate Angle between velocity vetor and vetor from pursuer to target
    vector_to_target = np.array([[position_target[0] - position_pursuer[0]], [position_target[1] - position_pursuer[1]]])
    
    # Flatten to work with
    flat_vtt = vector_to_target.flatten()
    flat_vel = velocity_pursuer.flatten()

    angle = np.arccos(np.dot(flat_vtt, flat_vel) / (np.linalg.norm(flat_vtt) * np.linalg.norm(flat_vel)))

    print("LOS ANGLE: %f" % angle)

    return angle

def calculate_new_conditions(velocity_pursuer, velocity_target, position_pursuer, position_target, acceleration):

    # Calculate new velocity and position
    velocity_pursuer = velocity_pursuer + acceleration
    position_pursuer = position_pursuer + velocity_pursuer

    print("PURSUER POS: x:%f y:%f" % (position_pursuer[0], position_pursuer[1]))

    velocity_target = velocity_target
    position_target = position_target + velocity_target

    print("TARGET POS: x:%f y:%f" % (position_target[0], position_target[1]))

    return (velocity_pursuer, velocity_target, position_pursuer, position_target)

def plot_position(velocity_pursuer, velocity_target, position_pursuer, position_target):

    # Define positions based on initial velocities and headings
    vel_pursuer = velocity_pursuer.flatten()
    vel_target = velocity_target.flatten()

    pos_pursuer = position_pursuer.flatten()
    pos_target = position_target.flatten()

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.quiver(
        pos_pursuer[0], pos_pursuer[1], vel_pursuer[0], vel_pursuer[1],
        angles='xy', scale_units='xy', scale=1, color='blue', label='Pursuer Velocity'
    )
    plt.quiver(
        pos_target[0], pos_target[1], vel_target[0], vel_target[1],
        angles='xy', scale_units='xy', scale=1, color='red', label='Target Velocity'
    )

    plt.xlim(-10, 240)
    plt.ylim(-10, 240)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Pursuer and Target Velocities")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()
    plt.show()

# Main Execution
if __name__ == "__main__":

    # Declare Variables
    time_iterations = 20
    vel_pursuer     = [np.array([[0], [0]])] * time_iterations
    vel_target      = [np.array([[0], [0]])] * time_iterations
    pos_pursuer     = [np.array([[0], [0]])] * time_iterations
    pos_target      = [np.array([[0], [0]])] * time_iterations
    acceleration    = [np.array([[0], [0]])] * time_iterations
    los_angle       = [np.array([[0], [0]])] * time_iterations

    vel_pursuer[0], vel_target[0], pos_pursuer[0], pos_target[0], acceleration[0] = generate_starting_conditions()

    for i in range(time_iterations - 1):

        
        print("\nITERATION %f" % i)

        los_angle[i] = calculate_los(vel_pursuer[i], pos_pursuer[i], pos_target[i])

        if i != 0:
            acceleration[i] = calculate_acceleration(vel_pursuer[i], vel_target[i], pos_pursuer[i], pos_target[i], los_angle[i], los_angle[i - 1])

        vel_pursuer[i + 1], vel_target[i + 1], pos_pursuer[i + 1], pos_target[i + 1] = calculate_new_conditions(vel_pursuer[i], vel_target[i], pos_pursuer[i], pos_target[i], acceleration[i])



    # plot_position(vel_pursuer[0], vel_target[0], pos_pursuer[0], pos_target[0])

    pass




