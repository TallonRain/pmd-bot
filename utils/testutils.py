import json
import random

with open('quiz/questions-en.json') as f:
    question_data = json.load(f)


def fetch_question(iteration):
    return question_data[iteration]['title']


def generate_unique_random_numbers(n, min_val, max_val):
    """Generates a set of n unique random numbers between min_val and max_val."""
    if n > max_val - min_val + 1:
        raise ValueError("Cannot generate more unique numbers than the range allows.")

    numbers = list(range(min_val, max_val + 1))
    random.shuffle(numbers)
    return numbers[:n]

