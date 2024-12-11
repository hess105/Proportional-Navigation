%% __________
%% Parameters
N = 3; % Navigation constant (typical values: 3-5)
dt = 0.001; % Time step for simulation
max_steps = 1000000; % Maximum number of iterations

%% ______________
%% Initialization
pursuer_pos = [0; 0];
target_pos = [0; 5000];

pursuer_velo = [10; 50];
target_velo = [50; 10];

%% _________________________
%% Storage for visualization

% Preallocation (essential to performance)
pursuer_trajectory = nan(max_steps, 2);
target_trajectory = nan(max_steps, 2);

% Assign initial conidtions
pursuer_trajectory(1,:) = pursuer_pos';
target_trajectory(1,:) = target_pos';

% Reset some variables in case of no clear
interception = [NaN,NaN];

%% _______________ 
%% Simulation loop
for step = 1:max_steps
    % Calculate relative position and velocity
    rel_pos = target_pos - pursuer_pos;
    rel_velo = target_velo - pursuer_velo;
    
    % Compute line-of-sight (LOS) angle
    los_angle = atan2(rel_pos(2), rel_pos(1));
    
    % Compute LOS rate (time derivative of LOS angle)
    los_rate = (rel_pos(1) * rel_velo(2) - rel_pos(2) * rel_velo(1)) / (norm(rel_pos)^2);
    
    % Compute required lateral acceleration (PN law)
    lateral_accel = N * norm(pursuer_velo) * los_rate;
    
    % Update pursuer velocity direction
    pursuer_heading = atan2(pursuer_velo(2), pursuer_velo(1));
    pursuer_heading = pursuer_heading + lateral_accel * dt / norm(pursuer_velo);
    
    % Update pursuer velocity
    pursuer_velo = norm(pursuer_velo) * [cos(pursuer_heading); sin(pursuer_heading)];
    
    % Update positions
    pursuer_pos = pursuer_pos + pursuer_velo * dt;
    target_pos = target_pos + target_velo * dt;
    
    % Save trajectories
    pursuer_trajectory(step, :) = pursuer_pos';
    target_trajectory(step, :) = target_pos';

    % Check if intercept occurred
    if norm(target_pos - pursuer_pos) < 0.1 % Threshold for interception
        interception = pursuer_pos';
        time = step * dt;
        fprintf('Intercept occurred at %.2f seconds (step %d)\n', time, step);
        break;
    end
end

%% _________________
%% Plot trajectories
figure;

plot(pursuer_trajectory(:,1), pursuer_trajectory(:,2), '-b', 'LineWidth', 2);
hold on;
plot(target_trajectory(:,1), target_trajectory(:,2), '-r', 'LineWidth', 2);
hold on;
plot(interception(1), interception(2), 'g*', 'MarkerSize', 10, 'LineWidth', 2);
legend('Pursuer', 'Target', 'Interception', 'Location', 'southeast');
xlabel('X Position');
ylabel('Y Position');
title('Proportional Navigation Guidance Position Map [N = 3]');
grid on;
