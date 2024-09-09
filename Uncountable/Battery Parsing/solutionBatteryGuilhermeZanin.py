import matplotlib.pyplot as plt
from pathlib import Path

# Read the data from file
file_path = Path(__file__).with_name('battery_parsing.txt')

# List for data of each cycle
cycle_data = []

#Opens and read the file
with open(file_path, 'r') as file:
    lines = file.readlines()
    # Read data from file
    for line in lines[0:]:
        if line.strip():  # If line is not empty
            parts = line.split() # gets each line data / split removes spacing
            if parts[0].isdigit():
                # reads the value in respective column, according to the column of interest
                half_cycle = int(parts[13])
                cycle_number = float(parts[16])
                capacity = float(parts[27])
                
                # Uses mod of 2 to check for alternance (Charge / Discharge)
                # Then appends to the data for graph
                cycle_type = 'Charge' if half_cycle % 2 == 0 else 'Discharge'
                cycle_data.append((cycle_number, capacity, cycle_type))

# Dictionary structure for the Max capacities for Charge and Discharge for each cycle
charge_cycle_capacities = {}
discharge_cycle_capacities = {}

# Extracting the Max capacties
# Iterates through cycle_data tuples and categorizes them into charge_cycle_capacities or discharge_cycle_capacities based on cycle_type.
# For each cycle_number, it updates or initializes the maximum capacity (capacity) for either charge or discharge.
for cycle_number, capacity, cycle_type in cycle_data:
    if cycle_type == 'Charge':
        if cycle_number not in charge_cycle_capacities:
            charge_cycle_capacities[cycle_number] = capacity
        else:
            charge_cycle_capacities[cycle_number] = max(charge_cycle_capacities[cycle_number], capacity)
    elif cycle_type == 'Discharge':
        if cycle_number not in discharge_cycle_capacities:
            discharge_cycle_capacities[cycle_number] = capacity
        else:
            discharge_cycle_capacities[cycle_number] = max(discharge_cycle_capacities[cycle_number], capacity)

# Data for plotting
charge_cycles = sorted(charge_cycle_capacities.keys())
charge_capacities = [charge_cycle_capacities[cycle] for cycle in charge_cycles]

discharge_cycles = sorted(discharge_cycle_capacities.keys())
discharge_capacities = [discharge_cycle_capacities[cycle] for cycle in discharge_cycles]

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(charge_cycles, charge_capacities, marker='o', linestyle='-', color='b', label='Charge')
plt.plot(discharge_cycles, discharge_capacities, marker='o', linestyle='-', color='r', label='Discharge')

plt.xlabel('Cycle Number')
plt.ylabel('Capacity (ma.h)')
plt.title('Battery Capacity (Charge/Discharge) over Cycles')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()