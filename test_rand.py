import math
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import rand


def test_generate_random_integers_range():
    vals = rand.generate_random_integers(-5, 5)
    assert len(vals) == 10
    assert all(-5 <= v <= 5 for v in vals)


def test_generate_random_floats_range():
    vals = rand.generate_random_floats(0.0, 1.0)
    assert len(vals) == 10
    assert all(0.0 <= v <= 1.0 for v in vals)


def test_monte_carlo_pi_accuracy():
    estimate = rand.monte_carlo_pi(10000)
    assert abs(estimate - math.pi) < 0.1

