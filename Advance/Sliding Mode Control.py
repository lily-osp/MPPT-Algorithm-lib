def sliding_mode_control(voltage, current, reference_voltage, step_size=0.05):
    error = reference_voltage - voltage
    sliding_surface = error * current

    # Adjust step size based on sliding surface
    if sliding_surface > 0:
        voltage += step_size
    else:
        voltage -= step_size
    return voltage
