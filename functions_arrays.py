import numpy as np

subject1_grades = np.array([88, 90, 75, 92, 85])
subject2_grades = np.array([92, 85, 78, 90, 88])

total_grades = subject1_grades + subject2_grades

print("Total grades:", total_grades)  # Output: Total grades: [180 175 153 182 173]

angles_degrees = np.array([0, 30, 45, 60, 90])
angles_radians = np.radians(angles_degrees)
sin_values = np.sin(angles_radians)

print("Sine of angles:", sin_values)  # Output: Sine of angles: [0. 0.5 0.70710678 0.8660254 1.]

def is_even(n):
    return n % 2 == 0

vectorized_is_even = np.vectorize(is_even)

numbers = np.array([1, 2, 3, 4, 5])
results = vectorized_is_even(numbers)

print("Results:", results)  # Output: Results: [False True False True False]

# Function to calculate percentage marks
def percentage_calc(percentage_marks):
    return (percentage_marks * 100) / 75

# Array of raw marks
raw_marks = np.array([35, 48, 60, 72, 75])

# Compute percentage using our function
percentage_calc = np.vectorize(percentage_calc)
percentage_marks = percentage_calc(raw_marks)

print("Raw Marks: ", raw_marks)
print("Percentage Marks: ", percentage_marks)

# Function to calculate the discount price 
def discount_price(price):
    if price >= 350:
        return price - (price * 0.30)  # 30% discount for prices above RM3
    else :
        return price - (price * 0.20)  # 20% discount

# Array of original prices
prices = np.array([100, 200, 300, 400, 500])

# Compute discounted prices using our function
discount_price = np.vectorize(discount_price)
discounted_prices = discount_price(prices)

print("Original Prices: ", prices)
print("Discounted Prices : ", discounted_prices)

# Array of temperatures in Celsius for 5 consecutive days
temperatures_c = np.array([20.5, 25.3, 19.6, 22.7, 24.1])

# TODO: Write a function to convert temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# TODO: Apply the function to the temperatures_c array and transform them to Fahrenheit scale
temperatures_f = celsius_to_fahrenheit(temperatures_c)

print("Temperatures in Celsius: ", temperatures_c)

# TODO: Print the transformed Fahrenheit temperatures
print("Temperatures in Fahrenheit: ", temperatures_f)

# Array of numbers
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# TODO: find squares of numbers
squares = numbers ** 2
# TODO: find square roots of numbers
square_roots = np.sqrt(numbers)
# TODO: print numbers, their squares and their square roots
print("Numbers: ", numbers)
print("Squares: ", squares)
print("Square Roots: ", square_roots)