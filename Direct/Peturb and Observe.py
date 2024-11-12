def perturb_and_observe(voltage, current, step_size=0.1):
    # Power calculation
    power = voltage * current

    # Change in power and voltage for next iteration
    delta_power = power - perturb_and_observe.prev_power
    delta_voltage = voltage - perturb_and_observe.prev_voltage

    # Adjust step size based on direction
    if delta_power > 0:
        voltage += step_size if delta_voltage > 0 else -step_size
    else:
        voltage -= step_size if delta_voltage > 0 else -step_size

    # Update previous values
    perturb_and_observe.prev_power = power
    perturb_and_observe.prev_voltage = voltage

    return voltage

perturb_and_observe.prev_power = 0
perturb_and_observe.prev_voltage = 0
