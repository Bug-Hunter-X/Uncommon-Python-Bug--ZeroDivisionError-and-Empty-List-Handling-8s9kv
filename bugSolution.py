def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    # Use decimal module for better accuracy
    from decimal import Decimal, getcontext
    getcontext().prec = 28 # Set precision
    average = Decimal(total) / Decimal(len(numbers))
    return float(average)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1, 0, 3, 4, 5]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zero is: {average_with_zero}")

my_list_with_floats = [1.1, 2.2, 3.3, 4.4, 5.5]
average_with_floats = calculate_average(my_list_with_floats)
print(f"The average of floats is: {average_with_floats}") 