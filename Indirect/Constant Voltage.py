def constant_voltage_mppt(voltage, target_voltage=18.0):
    if voltage < target_voltage:
        voltage += 0.1  # Step up voltage slightly
    elif voltage > target_voltage:
        voltage -= 0.1  # Step down voltage slightly
    return voltage
