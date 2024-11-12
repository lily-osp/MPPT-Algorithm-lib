import random

def genetic_algorithm_mppt(voltage_population, current_population, generations=10, mutation_rate=0.01):
    def fitness(voltage, current):
        return voltage * current  # Calculate power as fitness

    # Evolve population over generations
    for _ in range(generations):
        # Select parents based on fitness
        sorted_population = sorted(zip(voltage_population, current_population),
                                   key=lambda vc: fitness(vc[0], vc[1]), reverse=True)
        parents = sorted_population[:len(sorted_population)//2]

        # Crossover and mutation
        next_generation = []
        while len(next_generation) < len(voltage_population):
            parent1, parent2 = random.choice(parents), random.choice(parents)
            child_voltage = (parent1[0] + parent2[0]) / 2
            child_current = (parent1[1] + parent2[1]) / 2

            # Apply mutation
            if random.random() < mutation_rate:
                child_voltage += random.uniform(-0.1, 0.1)
                child_current += random.uniform(-0.1, 0.1)

            next_generation.append((child_voltage, child_current))

        voltage_population, current_population = zip(*next_generation)

    # Return best result in the final population
    best_voltage, _ = max(zip(voltage_population, current_population), key=lambda vc: fitness(vc[0], vc[1]))
    return best_voltage

# Initial population (sample values)
voltage_population = [random.uniform(15, 20) for _ in range(10)]
current_population = [random.uniform(1, 5) for _ in range(10)]
