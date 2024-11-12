import random

class Particle:
    def __init__(self, voltage, power):
        self.position = voltage
        self.best_position = voltage
        self.velocity = 0
        self.best_power = power

def fuzzy_logic_adjustment(current, prev_current, prev_error):
    # Calculate error and change in error
    error = current - prev_current
    delta_error = error - prev_error

    # Define simple fuzzy rules for adjustment based on error trends
    if error > 0 and delta_error > 0:
        adjustment = 0.1  # Increase voltage slightly
    elif error > 0 and delta_error < 0:
        adjustment = 0.05  # Smaller increase
    elif error < 0 and delta_error > 0:
        adjustment = -0.05  # Small decrease
    else:
        adjustment = -0.1  # Larger decrease

    return adjustment, error

def hybrid_pso_fuzzy_logic(voltage, current, particles, prev_voltage, prev_current, prev_error, iterations=10):
    # Initialize power and best power variables
    best_global_voltage = voltage
    best_global_power = voltage * current
    power = best_global_power

    # Particle Swarm Optimization phase
    for i in range(iterations):
        for particle in particles:
            # Calculate current power for each particle
            particle_power = particle.position * current
            if particle_power > particle.best_power:
                particle.best_power = particle_power
                particle.best_position = particle.position

            # Update global best position if needed
            if particle.best_power > best_global_power:
                best_global_power = particle.best_power
                best_global_voltage = particle.best_position

            # Update velocity and position for each particle
            particle.velocity = (0.5 * particle.velocity +
                                 random.uniform(0, 1) * (particle.best_position - particle.position) +
                                 random.uniform(0, 1) * (best_global_voltage - particle.position))
            particle.position += particle.velocity

    # Use PSO result as initial position for Fuzzy Logic fine-tuning
    adjusted_voltage = best_global_voltage
    fuzzy_adjustment, new_error = fuzzy_logic_adjustment(current, prev_current, prev_error)
    adjusted_voltage += fuzzy_adjustment

    # Update previous values for the next cycle
    prev_voltage = adjusted_voltage
    prev_current = current
    prev_error = new_error

    return adjusted_voltage, prev_voltage, prev_current, prev_error

# Initialize particles for PSO phase
particles = [Particle(voltage=17, power=17 * 2) for _ in range(5)]
prev_voltage = 17  # Initial voltage setting
prev_current = 2   # Initial current measurement
prev_error = 0     # Initial error setting

# Run hybrid MPPT control
voltage, prev_voltage, prev_current, prev_error = hybrid_pso_fuzzy_logic(prev_voltage, prev_current, particles, prev_voltage, prev_current, prev_error)
print(f"Adjusted voltage for MPPT: {voltage}")
