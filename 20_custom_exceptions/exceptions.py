# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


# Custom exception
class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return f"Age {age} is valid"

# Example usage with try...except
try:
    print(check_age(20))  # Output: Age 20 is valid
    print(check_age(15))  # Raises InvalidAgeError
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Age must be 18 or older