import numpy as np
from scipy.constants import pi 
from scipy.constants import kilo,mega
from CoolProp import CoolProp

def heat_conduction(pipe_radius, pipe_length, temperature_difference, material_thermal_conductivity):
    """
    Calculate heat transfer through a pipe using the heat conduction equation.

    Args:
        pipe_radius (float): Radius of the pipe (meters).
        pipe_length (float): Length of the pipe (meters).
        temperature_difference (float): Temperature difference across the pipe (Kelvin).
        material_thermal_conductivity (float): Thermal conductivity of the pipe material (W/(m*K)).

    Returns:
        float: Heat transfer rate (Watts).
    """
    surface_area = 2 * pi * pipe_radius * pipe_length
    heat_transfer_rate = material_thermal_conductivity * surface_area * temperature_difference / pipe_length
    #kA/L * dT
    return heat_transfer_rate

def main():
    # Parameters
    pipe_radius = 0.05  # 1 cm
    pipe_length = 5.0  # 10 meters
    temperature_difference = 50.0  # 50 Kelvin
    material_thermal_conductivity = 200 * mega  # Copper thermal conductivity (W/(m*K))

    # Calculate heat transfer
    heat_transfer_rate = heat_conduction(pipe_radius, pipe_length, temperature_difference, material_thermal_conductivity)

    # Display result
    print(f"Heat Transfer Rate: {heat_transfer_rate} Watts")
    print(f"Mega Constant: {mega} -")

if __name__ == "__main__":
    main()
