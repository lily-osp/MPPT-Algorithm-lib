def incremental_conductance(voltage, current, step_size=0.1):
    dV = voltage - incremental_conductance.prev_voltage
    dI = current - incremental_conductance.prev_current

    if dV == 0:
        return voltage  # No change in voltage, return the current voltage

    # Incremental conductance
    dP_dV = current / voltage
    inc_conductance = dI / dV

    if abs(dP_dV - inc_conductance) < 1e-3:
        return voltage
    elif dP_dV > inc_conductance:
        voltage += step_size
    else:
        voltage -= step_size

    incremental_conductance.prev_voltage = voltage
    incremental_conductance.prev_current = current
    return voltage

incremental_conductance.prev_voltage = 0
incremental_conductance.prev_current = 0
