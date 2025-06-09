# guard.py

import random
import rand

def main():
    print("Welcome to ChatGPT Codex")
    a: int = -10
    b: int = 30
    seed = 17
    random.seed(seed)
    my_ran_ints: list = rand.generate_random_integers(a, b)
    print("Random integers:", my_ran_ints)

    random.seed(seed)
    my_ran_floats: list = rand.generate_random_floats(0.0, 1.0)
    print("Random floats:", my_ran_floats)

    pi_estimate: float = rand.monte_carlo_pi(10_000_000)
    print("Monte Carlo pi:", pi_estimate)

if __name__ == "__main__":
    main()

