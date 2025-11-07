import random
import sys
import time


def read_input(prompt):
    """Read input from the user, normalize and return lowercase stripped string."""
    return input(prompt).strip().lower()


def random_event(chance_percent):
    """Return True with chance_percent probability (0-100)."""
    return random.randint(0, 99) < chance_percent


def slow_println(s, ms):
    """Print a line and sleep for ms milliseconds (flush stdout first)."""
    print(s)
    sys.stdout.flush()
    time.sleep(ms / 1000.0)
