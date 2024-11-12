def temperature_based_mppt(temperature, voltage_ref=12.0):
    # Adjust reference voltage based on temperature
    if temperature > 25:
        voltage_ref -= 0.1 * (temperature - 25)
    else:
        voltage_ref += 0.1 * (25 - temperature)
    return voltage_ref
