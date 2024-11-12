def hybrid_po_cv(voltage, current, target_voltage=18.0, step_size=0.05):
    # P&O approach
    power = voltage * current
    delta_power = power - hybrid_po_cv.prev_power
    if delta_power > 0:
        voltage += step_size
    else:
        voltage -= step_size

    # Constant voltage refinement
    if abs(voltage - target_voltage) > 0.5:
        voltage = target_voltage

    hybrid_po_cv.prev_power = power
    return voltage

hybrid_po_cv.prev_power = 0
