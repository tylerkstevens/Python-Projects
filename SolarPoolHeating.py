#Remake of ME461 HW3, orginally coded in EES. Trying to implement the model in python

import numpy as np
from scipy.optimize import fsolve
from scipy.constants import pi 
from scipy.constants import kilo,mega
from CoolProp import CoolProp
import matplotlib.pyplot as plt
import pint

# Create a unit registry
ureg = pint.UnitRegistry()
ureg = pint.UnitRegistry()
ureg.define('dollar = 1.00 USD = $')

# Define system knowns
eta_p = 0.4  # pump efficiency
eta_h = 0.95  # heater efficiency
v_w = 0.001 * ureg.meter**3 / ureg.kilogram  # specific volume of pool water
c_w = 4200 * ureg.joule / ureg.kilogram / ureg.kelvin  # specific heat capacity of water
P_o = (14.7 * ureg.psi).to(ureg.pascal)  # pressure in pascals
ec = 0.12 * ureg.dollar / ureg.kilowatt_hour
ngc = 0.04 * ureg.dollar / ureg.kilowatt_hour

## Convert Temperature Function from F to K
def convert_temperature(value, from_unit, to_unit):
    return ureg.Quantity(value, from_unit).to(ureg.kelvin)

## Temp Unit Conversions
T_o = convert_temperature(70, 'degF', 'kelvin')  # temperature in kelvin
T_pool = convert_temperature(80, 'degF', 'kelvin')  # temperature in kelvin
T_f = convert_temperature(1200, 'degF', 'kelvin')  # temperature in kelvin

## Other Known Parameters
SF = 950 *ureg.watt / ureg.meter**2    #solar flux
A_col = 6 *ureg.meter**2               #area 
UA = 120 *ureg.watt / ureg.kelvin      #overall heat transfer
#W_dot_sc = SF*A_col #

## Pump Curve
N = 800                                             #[rpm]    
DELTA_P_dh = 150*N                                  #[Pa] dead head pressure
Vol_dot_oc = 5E-7*N                                 #[m3/s] open circuit flow rate
# Define the system of equations
def equations(Vol_dot):
    DELTA_P_h = 3E12*Vol_dot**2              #[Pa-s^2/m^6] Water System Heater Curve
    DELTA_P = DELTA_P_dh * (1 - (Vol_dot / Vol_dot_oc))
    DELTA_P_col = 5E12*Vol_dot**2            #[Pa-s^2/m^6] Solar Flux Collector System Curve
    DELTA_P_sys = DELTA_P_h + DELTA_P_col
    return np.array([float(DELTA_P - DELTA_P_sys)])
# Initial guess for Vol_dot
initial_guess = 1E-7
# Solve the system of equations
solution = fsolve(equations, initial_guess)

# Display the result
Vol_dot = solution[0]
print("Vol_dot:", Vol_dot, "m^3/s")

#Fixed Parameters
m_dot = Vol_dot/v_w.magnitude
print("m_dot:", m_dot, "kg/s")
#Mass Balance
# mass flow rate constant for all states: m = m4 = m3 = m2 = m1

#State 4-1

#State 1 - pump inlet
T1 = T_pool
P1 = P_o
u1 = c_w*T1
h1 = u1 + v_w*P1

"""
# Display the converted values
print("eta_p:", eta_p)
print("eta_h:", eta_h)
print("v_w:", v_w.magnitude)
print("c_w:", c_w.magnitude)
print("P_o:", P_o.magnitude)
print("T_o:", T_o.magnitude)
print("T_pool:", T_pool.magnitude)
print("T_f:", T_f.magnitude)
print("ec:",ec.magnitude)
print("ngc:",ngc.magnitude)
print("Solar Flux:", SF.magnitude)
print("A_col:",A_col.magnitude)
print("UA:",UA.magnitude)
print("DELTA_P_dh:",DELTA_P_dh)
print("Vol_dot_oc:",Vol_dot_oc)
print("DELTA_P_h:",DELTA_P_h)
print("DELTA_P_col:",DELTA_P_col)
print("DELTA_P_sys:",DELTA_P_sys)
"""