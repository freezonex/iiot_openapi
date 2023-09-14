import random


# Function to generate a random float within a range
def random_float(min_value, max_value):
    return round(min_value + (max_value - min_value) * random.random(), 1)
