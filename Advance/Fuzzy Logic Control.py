def fuzzy_logic_control(voltage, current):
    # Initialize membership functions for error and change in error
    error = current - fuzzy_logic_control.prev_current
    delta_error = error - fuzzy_logic_control.prev_error

    # Define fuzzy rules and membership function based outputs
    if error > 0 and delta_error > 0:
        adjustment = 0.1
    elif error > 0 and delta_error < 0:
        adjustment = 0.05
    elif error < 0 and delta_error > 0:
        adjustment = -0.05
    else:
        adjustment = -0.1

    # Adjust voltage based on the fuzzy control
    voltage += adjustment
    fuzzy_logic_control.prev_current = current
    fuzzy_logic_control.prev_error = error
    return voltage

fuzzy_logic_control.prev_current = 0
fuzzy_logic_control.prev_error = 0
