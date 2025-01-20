#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys

def parse_file(file_path):
    """Parse the file to extract the parameters for the best-fit line."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)

    # Find the first line below "# Log(likelihood)\tnuB\tnuF\tTB\tTF\ttheta"
    for i, line in enumerate(lines):
        if line.strip().startswith("# Log(likelihood)"):
            try:
                params_line = lines[i + 1].strip()
                _, nuB, nuF, TB, TF, _ = map(float, params_line.split())
                return nuB, nuF, TB, TF
            except (IndexError, ValueError):
                print("Error: Invalid file format. Could not extract parameters.")
                sys.exit(1)

    print("Error: Could not find parameter line in the file.")
    sys.exit(1)

def theoretical_population(t, bottleneck_time, recovery_time):
    """Calculate the theoretical population size at time t."""
    if t < bottleneck_time:
        return 10  # Population size before bottleneck
    elif t > 0.5:
        return 10  # Population size during bottleneck
    else:
        return 5 # Population size after recovery

def estimated_population(t, nuB, nuF, TB, TF):
    """Calculate the estimated population size at time t based on model parameters."""
    if t > TB+TF:
        return 10  # Population size before bottleneck
    elif t < TF:
        return nuF * 10  # Population size during bottleneck
    else:
        return nuB * 10  # Population size after recovery

def plot_population_dynamics(nuB, nuF, TB, TF, bottleneck_time):
    """Plot the theoretical and estimated population dynamics."""
    time = np.linspace(0, 5, 1000)  # Time from 0 to slightly beyond recovery

    # Compute theoretical and estimated population sizes
    theoretical = [theoretical_population(t, bottleneck_time, TF) for t in time]
    estimated = [estimated_population(t, nuB, nuF, TB, TF) for t in time]

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time, theoretical, label="Théorique", linestyle="--", color="blue")
    plt.plot(time, estimated, label="Estimé", color="red")

    # Add labels and legend
    plt.xlabel("Temps (en unités de Ne générations)")
    plt.ylabel("Taille de la population")
    plt.title("Dynamique de la population : théorique vs estimée")
    plt.legend()
    plt.grid(True)
    plt.show()

def calculate_weighted_rmsd_log_time(theoretical, estimated, time, epsilon=1e-3, decay_rate=5):
   
    # Logarithmic time transformation
    transformed_time = np.log(time + epsilon)

    # Calculate weights based on the original time
    weights = np.exp(-decay_rate * time)
    
    # Calculate differences
    differences = np.array(theoretical) - np.array(estimated)

    # Apply weights to the squared differences
    weighted_squared_differences = (differences ** 2) * weights

    # Calculate the weighted RMSD on the transformed time scale
    rmsd = np.sqrt(np.mean(weighted_squared_differences))

    return rmsd

def compute_weighted_rmsd_log_time(nuB, nuF, TB, TF, bottleneck_time, epsilon=1e-3, decay_rate=5):
    """
    Compute weighted RMSD with log time between theoretical and estimated
    population dynamics.
    """
    time = np.linspace(0, 1, 1000)
    theoretical = [theoretical_population(t, bottleneck_time, TF) for t in time]
    estimated = [estimated_population(t, nuB, nuF, TB, TF) for t in time]
    return calculate_weighted_rmsd_log_time(theoretical, estimated, time, epsilon, decay_rate)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script_name.py <bottleneck_time> <file_path>")
        sys.exit(1)

    file_path = sys.argv[2]
    try:
        bottleneck_time = float(sys.argv[1])
    except ValueError:
        print("Error: bottleneck_time must be a number.")
        sys.exit(1)
    
    nuB, nuF, TB, TF = parse_file(file_path)
    plot_population_dynamics(nuB, nuF, TB, TF, bottleneck_time)
    rmsd_value = compute_weighted_rmsd_log_time(nuB, nuF, TB, TF, bottleneck_time)
    print(f"Weighted RMSD: {rmsd_value}")
