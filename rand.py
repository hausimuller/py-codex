import random
from typing import List

def generate_random_integers(a: int, b: int) -> List[int]:
    """Generate a list of 10 random integers between a and b (inclusive)."""
    """Generate a list of 10 random integers between ``a`` and ``b`` (inclusive)."""
    return [random.randint(a, b) for _ in range(10)]


def generate_random_floats(a: float, b: float) -> List[float]:
    """Generate a list of 10 random floating point numbers between ``a`` and ``b``."""
    return [random.uniform(a, b) for _ in range(10)]


def monte_carlo_pi(num_samples: int) -> float:
    """Approximate ``pi`` using a Monte Carlo simulation with ``num_samples`` points."""
    inside = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / num_samples

# Example usage:
if __name__ == "__main__":
    print(generate_random_integers(1, 100))
    print("Random integers:", generate_random_integers(1, 100))
    print("Random floats:", generate_random_floats(0.0, 1.0))
    print("Monte Carlo pi:", monte_carlo_pi(1_000_000))

