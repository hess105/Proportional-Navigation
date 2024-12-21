%% Initialization
% Rocket Parameters
rocket_mass = 0.034; % [kg]
engine_mass = 0.024; % [kg]
total_mass = engine_mass + rocket_mass; % [kg]

average_thrust = 5; % [N]
burn_time = 0.8; % [s]

% Environmental Constants
g = 9.81; % [m/s^2] gravitational acceleration
rho = 1.225; % [kg/m^3] air density
Cd = 0.75; % Drag coefficient (assumed typical value for a model rocket)
A = 0.001256; % [m^2] cross-sectional area (e.g., diameter of 0.04 m)
wind = [0; 0]; % [m/s] wind velocity (assumed negligible in this example)

% Simulation Settings
max_steps = 1000;
dt = 0.01; % [s] timestep

% Initialize State Variables
time = 0; % [s]
altitude = 0; % [m]
velocity = 0; % [m/s]
mass = total_mass; % [kg]

% Thrust Parameters
thrust_duration = burn_time;
thrust_profile = @(t) (t <= thrust_duration) * average_thrust; % Thrust is constant during burn

% Arrays for Storing Results
time_array = zeros(max_steps, 1);
altitude_array = zeros(max_steps, 1);
velocity_array = zeros(max_steps, 1);
altitude_no_drag_array = zeros(max_steps, 1);

%% Simulation Loop
for step = 1:max_steps
    % Record current state
    time_array(step) = time;
    altitude_array(step) = altitude;
    velocity_array(step) = velocity;

    % Calculate forces with drag
    thrust = thrust_profile(time); % [N]
    gravitational_force = mass * g; % [N]
    drag_force = 0.5 * rho * Cd * A * velocity^2 * sign(velocity); % [N]
    net_force = thrust - gravitational_force - drag_force; % [N]

    % Update acceleration, velocity, and position with drag
    acceleration = net_force / mass; % [m/s^2]
    velocity = velocity + acceleration * dt; % [m/s]
    altitude = altitude + velocity * dt; % [m]

    % Calculate altitude without drag
    net_force_no_drag = thrust - gravitational_force; % [N]
    acceleration_no_drag = net_force_no_drag / mass; % [m/s^2]
    velocity_no_drag = velocity_array(max(step - 1, 1)) + acceleration_no_drag * dt; % [m/s]
    altitude_no_drag_array(step) = altitude_no_drag_array(max(step - 1, 1)) + velocity_no_drag * dt; % [m]

    % Decrease mass linearly during thrust phase
    if time < thrust_duration
        mass = total_mass - ((engine_mass / thrust_duration) * time);
    end

    % Stop simulation if rocket hits the ground
    if altitude <= 0 && time > 0
        break;
    end

    % Increment time
    time = time + dt;
end

%% Trim Results
valid_steps = step;
time_array = time_array(1:valid_steps);
altitude_array = altitude_array(1:valid_steps);
velocity_array = velocity_array(1:valid_steps);
altitude_no_drag_array = altitude_no_drag_array(1:valid_steps);

%% Plot Results
figure;
subplot(2, 1, 1);
plot(time_array, altitude_array, 'b', 'DisplayName', 'With Drag');
hold on;
plot(time_array, altitude_no_drag_array, 'r--', 'DisplayName', 'No Drag');
hold off;
grid on;
legend;
title('Rocket Altitude vs. Time');
xlabel('Time [s]');
ylabel('Altitude [m]');

subplot(2, 1, 2);
plot(time_array, velocity_array);
grid on;
title('Rocket Velocity vs. Time');
xlabel('Time [s]');
ylabel('Velocity [m/s]');
