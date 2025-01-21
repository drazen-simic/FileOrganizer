import random
"""
The random module in Python is part of the standard library and provides functions to generate random numbers and perform random operations. 
It is commonly used for simulations, generating random test data,
creating randomized algorithms, and more."""
# 1. Random Number Generation
print("Random float (0.0 to 1.0):", random.random())
print("Random integer (1 to 10):", random.randint(1, 10))
print("Random float (1.5 to 5.5):", random.uniform(1.5, 5.5))

# 2. Working with Sequences
colors = ['red', 'blue', 'green']
print("Random choice from list:", random.choice(colors))
print("Random multiple choices:", random.choices(colors, k=2))

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled list:", cards)

# 3. Sampling
print("Random sample of 3 elements:", random.sample(range(10), 3))

# 4. Controlling Randomness
random.seed(42)
print("Seeded random float:", random.random())

# 5. Distributions
print("Gaussian random number (mean=0, stddev=1):", random.gauss(0, 1))


# Program: Randomized Quiz Question Selector
questions = [
    "What is the capital of France?",
    "What is 2 + 2?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?"
]

# Shuffle questions
random.shuffle(questions)

# Display 3 random questions
print("Here are your random quiz questions:")
for question in random.sample(questions, 3):
    print(f"- {question}")
