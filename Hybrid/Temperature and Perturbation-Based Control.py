def hybrid_temp_perturb(voltage, current, temperature, step_size=0.05):
    power = voltage * current
    delta_power = power - hybrid_temp_perturb.prev_power

    # Perturbation step
    if delta_power > 0:
        voltage += step_size
    else:
        voltage -= step_size

    # Temperature refinement
    if temperature > 25:
        voltage -= 0.1 * (temperature - 25)

    hybrid_temp_perturb.prev_power = power
    return voltage

hybrid_temp_perturb.prev_power = 0
