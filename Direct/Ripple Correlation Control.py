def ripple_correlation_control(voltage, current, duty_cycle, step_size=0.1):
    power = voltage * current
    delta_power = power - ripple_correlation_control.prev_power

    if delta_power > 0:
        duty_cycle += step_size
    else:
        duty_cycle -= step_size

    ripple_correlation_control.prev_power = power
    return duty_cycle

ripple_correlation_control.prev_power = 0
