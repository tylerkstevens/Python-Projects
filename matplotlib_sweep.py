import numpy as np
import matplotlib.pyplot as plt

# Define a simple mathematical model
def model(x, parameter):
    return x * parameter

# Sweep a parameter and plot the results
def sweep_and_plot():
    # Define the range of parameter values to sweep
    parameter_values = np.linspace(1, 5, 10)

    # Initialize lists to store results
    x_values = []
    y_values = []

    # Sweep the parameter values
    for parameter in parameter_values:
        # Generate x values (e.g., time points)
        x = np.linspace(0, 10, 100)

        # Calculate y values using the model
        y = model(x, parameter)

        # Store results
        x_values.append(x)
        y_values.append(y)

        # Plot the results for each parameter value
        plt.plot(x, y, label=f'Parameter = {parameter}')

    # Customize the plot
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sweeping Parameters and Plotting Results')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

# Call the function to sweep and plot
sweep_and_plot()
