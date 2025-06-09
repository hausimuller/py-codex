import random
from typing import List

def generate_random_integers(a: int, b: int) -> List[int]:
    """Generate a list of 10 random integers between a and b (inclusive)."""
    return [random.randint(a, b) for _ in range(10)]

# Example usage:
if __name__ == "__main__":
    print(generate_random_integers(1, 100))
