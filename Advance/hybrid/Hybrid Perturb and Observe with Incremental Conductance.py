def perturb_observe(voltage, current, prev_voltage, prev_power):
    # Calculate current power
    power = voltage * current
    delta_power = power - prev_power

    # Basic P&O logic to perturb voltage
    if delta_power > 0:
        voltage += 0.1  # Small increase
    else:
        voltage -= 0.1  # Small decrease

    # Update previous values
    prev_voltage = voltage
    prev_power = power

    return voltage, prev_voltage, prev_power

def incremental_conductance(voltage, current, prev_voltage, prev_current):
    # Calculate incremental conductance values
    delta_I = current - prev_current
    delta_V = voltage - prev_voltage

    # Apply Incremental Conductance logic
    if delta_V != 0 and delta_I / delta_V == -current / voltage:
        adjustment = 0  # Already at MPP
    elif delta_V == 0 or delta_I / delta_V > -current / voltage:
        adjustment = 0.1  # Move right on the power curve
    else:
        adjustment = -0.1  # Move left on the power curve

    # Update previous values
    prev_voltage = voltage
    prev_current = current

    return voltage + adjustment, prev_voltage, prev_current

def hybrid_po_inc(voltage, current, prev_voltage, prev_power, prev_current, threshold=0.01):
    # Use P&O to reach near MPP
    voltage, prev_voltage, prev_power = perturb_observe(voltage, current, prev_voltage, prev_power)

    # Switch to Incremental Conductance for fine adjustment near MPP
    if abs(prev_power - voltage * current) < threshold:
        voltage, prev_voltage, prev_current = incremental_conductance(voltage, current, prev_voltage, prev_current)

    return voltage, prev_voltage, prev_power, prev_current

# Initialize previous values
voltage = 17
current = 2
prev_voltage = voltage
prev_power = voltage * current
prev_current = current

# Run hybrid MPPT control
voltage, prev_voltage, prev_power, prev_current = hybrid_po_inc(voltage, current, prev_voltage, prev_power, prev_current)
print(f"Adjusted voltage for MPPT: {voltage}")
