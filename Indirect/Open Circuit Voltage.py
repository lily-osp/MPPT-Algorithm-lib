def open_circuit_voltage_mppt(open_circuit_voltage, k=0.8):
    # Use a constant factor to set MPP voltage
    mpp_voltage = k * open_circuit_voltage
    return mpp_voltage
