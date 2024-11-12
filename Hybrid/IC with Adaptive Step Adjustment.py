def hybrid_ic_adaptive(voltage, current, step_size=0.05, min_step=0.01):
    dV = voltage - hybrid_ic_adaptive.prev_voltage
    dI = current - hybrid_ic_adaptive.prev_current

    if dV == 0:
        return voltage  # No change in voltage

    dP_dV = current / voltage
    inc_conductance = dI / dV

    if abs(dP_dV - inc_conductance) < 1e-3:
        return voltage  # MPP is reached
    elif dP_dV > inc_conductance:
        step_size = max(step_size / 2, min_step)
        voltage += step_size
    else:
        step_size = max(step_size / 2, min_step)
        voltage -= step_size

    hybrid_ic_adaptive.prev_voltage = voltage
    hybrid_ic_adaptive.prev_current = current
    return voltage

hybrid_ic_adaptive.prev_voltage = 0
hybrid_ic_adaptive.prev_current = 0
