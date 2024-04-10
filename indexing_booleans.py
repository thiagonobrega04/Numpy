import numpy as np

# A boolean index for even numbers
array_1d = np.array([8, 4, 7, 3, 4, 11])
even_index = array_1d % 2 == 0
even_numbers = array_1d[even_index]
print(even_numbers)  # Output: [8 4 4]

# A boolean index for even numbers
array_1d = np.array([8, 4, 7, 3, 4, 11])
even_numbers = array_1d[array_1d % 2 == 0]
print(even_numbers)  # Output: [8 4 4]

# A combined boolean index for even numbers > 5
array_1d = np.array([8, 4, 7, 3, 4, 11])
even_numbers_greater_than_five = array_1d[(array_1d % 2 == 0) & (array_1d > 5)]
print(even_numbers_greater_than_five)  # Output: [8]

# A combined boolean index for even numbers or numbers > 5
array_1d = np.array([8, 4, 7, 3, 4, 11])
even_numbers_or_numbers_greater_than_five = array_1d[(array_1d % 2 == 0) | (array_1d > 5)]
print(even_numbers_or_numbers_greater_than_five)  # Output: [8 4 7 4 11]

# Select elements at index 0, 1, 2
array_1d = np.array([1, 2, 3, 4, 5, 6])
first_three = array_1d[0:3]
print(first_three)  # Output: [1 2 3]

# Select elements at odd indices 1, 3, 5, ...
array_1d = np.array([1, 2, 3, 4, 5, 6])
every_second = array_1d[1:6:2]
print(every_second)  # Output: [2 4 6]

# Create a NumPy array of ages
ages = np.array([15, 18, 16, 19, 36, 34, 27, 21, 23, 25])

# Select adults age under 30 years
adults = ages[(ages > 18) & (ages < 30)]
print("Adults:", adults)

# Create a NumPy array
weight = np.array([12, 15, 11, 9, 23, 10, 12, 20, 25, 25, 8, 15, 4])

# TODO: Select weights greater than 20 or less than 10
weights_over_twenty = weight[(weight >= 20) | (weight <= 10)]
print("Weights over twenty: ", weights_over_twenty)

badges = np.array([12, 14, 15, 20, 32, 33, 40, 42])

# TODO: Using a condition-based selection, filter badges that has even number lower than 33
evens_lower_than_thirty = badges[(badges % 2 == 0) & (badges < 33)]
print("Badge evens lower than 33: ", evens_lower_than_thirty)

# TODO: Print the filtered numbers.
first_three = evens_lower_than_thirty[0:3]
print(first_three)