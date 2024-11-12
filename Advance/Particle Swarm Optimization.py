import random

# Define particle class for PSO
class Particle:
    def __init__(self, voltage, power):
        self.position = voltage  # Position in search space (voltage)
        self.best_position = voltage
        self.velocity = 0
        self.best_power = power

def particle_swarm_optimization(voltage, current, particles, iterations=10):
    power = voltage * current
    for i in range(iterations):
        for particle in particles:
            # Calculate new power and compare with best power
            new_power = voltage * current
            if new_power > particle.best_power:
                particle.best_power = new_power
                particle.best_position = particle.position

            # Update velocity and position
            particle.velocity = (0.5 * particle.velocity +
                                 random.uniform(0, 1) * (particle.best_position - particle.position))
            particle.position += particle.velocity
            voltage = particle.position
    return voltage

# Initialize particles for PSO
particles = [Particle(voltage=17, power=voltage * current) for _ in range(5)]
