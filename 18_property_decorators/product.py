# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
    

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

# Example usage
product = Product("Laptop", 1000)

# Get price using property
print(product.price)  # Output: 1000

# Update price using setter
product.price = 1200
print(product.price)  # Output: 1200

# Attempt to set invalid price
try:
    product.price = -50
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Delete price using deleter
del product.price
try:
    print(product.price)  # Raises AttributeError: 'Product' object has no attribute '_price'
except AttributeError as e:
    print(e)  # Output: 'Product' object has no attribute '_price'