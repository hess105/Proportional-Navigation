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

N = 5

# Functions

def generate_starting_conditions():
    
    # Initial Velocities
    velocity_pursuer = np.array([[10], [10]])
    velocity_target = np.array([[6], [2]])

    # Initial Positions
    position_pursuer = np.array([[0], [0]])
    position_target = np.array([[50], [100]])

    # Initial Acceleration
    acceleration = np.array([[0], [0]])

    return (velocity_pursuer, velocity_target, position_pursuer, position_target, acceleration)

def calculate_acceleration(velocity_pursuer, velocity_target, los_angle, los_angle_old):
    # Calculate Target Velocity relative to pursuer
    relative_velocity_target = velocity_target - velocity_pursuer
    delta_los = (los_angle - los_angle_old) 
    # Calculate Acceleration
    acceleration = N * relative_velocity_target * delta_los

    print(f"ACCELERATION: x:{acceleration[0].item():.2f} y:{acceleration[1].item():.2f}")

    return acceleration

def calculate_los(velocity_pursuer, position_pursuer, position_target):

    # Calculate Angle between velocity vetor and vetor from pursuer to target
    vector_to_target = np.array([[position_target[0] - position_pursuer[0]], [position_target[1] - position_pursuer[1]]])
    
    # Flatten to work with
    flat_vtt = vector_to_target.flatten()
    flat_vel = velocity_pursuer.flatten()

    angle = np.arccos(np.dot(flat_vtt, flat_vel) / (np.linalg.norm(flat_vtt) * np.linalg.norm(flat_vel)))

    print(f"LOS ANGLE: {angle:.2f}")

    return angle

def calculate_new_conditions(velocity_pursuer, velocity_target, position_pursuer, position_target, acceleration):

    # Calculate new velocity and position
    velocity_pursuer = velocity_pursuer + acceleration
    position_pursuer = position_pursuer + velocity_pursuer

    print(f"PURSUER POS: x:{position_pursuer[0].item():.2f} y:{position_pursuer[1].item():.2f}")

    velocity_target = velocity_target
    position_target = position_target + velocity_target

    print(f"TARGET POS: x:{position_target[0].item():.2f} y:{position_target[1].item():.2f}")

    return (velocity_pursuer, velocity_target, position_pursuer, position_target)

def plot_positions_and_velocities(pos_pursuer, pos_target, vel_pursuer, vel_target):
    """
    Plot the positions and velocities of the pursuer and target.

    Args:
        pos_pursuer (list of np.ndarray): List of pursuer positions at each time step.
        pos_target (list of np.ndarray): List of target positions at each time step.
        vel_pursuer (list of np.ndarray): List of pursuer velocities at each time step.
        vel_target (list of np.ndarray): List of target velocities at each time step.
    """
    plt.figure(figsize=(10, 6))
    plt.title("Pursuer and Target Trajectories with Velocities")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    # Extract positions and velocities into separate lists for easier plotting
    pursuer_x = [p[0, 0] for p in pos_pursuer]
    pursuer_y = [p[1, 0] for p in pos_pursuer]
    target_x = [t[0, 0] for t in pos_target]
    target_y = [t[1, 0] for t in pos_target]

    # Plot trajectories
    plt.plot(pursuer_x, pursuer_y, 'b-', label="Pursuer Trajectory")
    plt.plot(target_x, target_y, 'r-', label="Target Trajectory")

    # Add velocity vectors at each step
    for i in range(len(pos_pursuer)):
        plt.arrow(
            pursuer_x[i],
            pursuer_y[i],
            vel_pursuer[i][0, 0] * 0.1,  # Scale velocity for visualization
            vel_pursuer[i][1, 0] * 0.1,
            color='blue',
            head_width=2,
            alpha=0.6,
            label="Pursuer Velocity" if i == 0 else None
        )
        plt.arrow(
            target_x[i],
            target_y[i],
            vel_target[i][0, 0] * 0.1,
            vel_target[i][1, 0] * 0.1,
            color='red',
            head_width=2,
            alpha=0.6,
            label="Target Velocity" if i == 0 else None
        )

    plt.legend()
    plt.grid()
    plt.show()


# Main Execution
if __name__ == "__main__":

    # Declare Variables
    time_iterations = 15
    vel_pursuer     = [np.array([[0], [0]])] * time_iterations
    vel_target      = [np.array([[0], [0]])] * time_iterations
    pos_pursuer     = [np.array([[0], [0]])] * time_iterations
    pos_target      = [np.array([[0], [0]])] * time_iterations
    acceleration    = [0] * time_iterations # applied perpendicular to velocity
    los_angle       = [np.array([[0], [0]])] * time_iterations

    vel_pursuer[0], vel_target[0], pos_pursuer[0], pos_target[0], acceleration[0] = generate_starting_conditions()

    for i in range(time_iterations - 1):

        print(f"\nITERATION: {i}")

        # Calculate Line of Sight
        los_angle[i] = calculate_los(vel_pursuer[i], pos_pursuer[i], pos_target[i])

        # Calculate Acceleration
        if i != 0:
            acceleration[i] = calculate_acceleration(vel_pursuer[i], vel_target[i], los_angle[i], los_angle[i - 1])

        # Calculate new velocity and position
        vel_pursuer[i + 1], vel_target[i + 1], pos_pursuer[i + 1], pos_target[i + 1] = calculate_new_conditions(vel_pursuer[i], vel_target[i], pos_pursuer[i], pos_target[i], acceleration[i])

        if i > 8:
            vel_target[i+1] = np.array([[2], [6]])

    # Plot Results
    plot_positions_and_velocities(pos_pursuer, pos_target, vel_pursuer, vel_target)


    pass




