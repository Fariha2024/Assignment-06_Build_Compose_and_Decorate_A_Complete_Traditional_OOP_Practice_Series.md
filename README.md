# Python OOP Practice Series

A complete collection of Python assignments covering fundamental Object-Oriented Programming concepts through practical implementation.

## Project Structure
oop_practice_series/
├── 01_self/ # Using self keyword
│ ├── init.py
│ └── student.py
├── 02_cls/ # Using cls keyword
│ ├── init.py
│ └── counter.py
├── 03_public/ # Public variables/methods
│ ├── init.py
│ └── car.py
├── 04_class_vars_methods/ # Class variables/methods
│ ├── init.py
│ └── bank.py
├── 05_static/ # Static methods
│ ├── init.py
│ └── math_utils.py
├── 06_constructors_destructors/ # Constructors/destructors
│ ├── init.py
│ └── logger.py
├── 07_access_modifiers/ # Access modifiers
│ ├── init.py
│ └── employee.py
├── 08_super/ # super() function
│ ├── init.py
│ └── inheritance.py
├── 09_abstract/ # Abstract classes
│ ├── init.py
│ └── shapes.py
├── 10_instance_methods/ # Instance methods
│ ├── init.py
│ └── dog.py
├── 11_class_methods/ # Class methods
│ ├── init.py
│ └── book.py
├── 12_static_methods/ # Static methods
│ ├── init.py
│ └── temperature.py
├── 13_composition/ # Composition
│ ├── init.py
│ └── car_engine.py
├── 14_aggregation/ # Aggregation
│ ├── init.py
│ └── department_employee.py
├── 15_mro/ # Method Resolution Order
│ ├── init.py
│ └── diamond_inheritance.py
├── 16_function_decorators/ # Function decorators
│ ├── init.py
│ └── decorators.py
├── 17_class_decorators/ # Class decorators
│ ├── init.py
│ └── class_decorators.py
├── 18_property_decorators/ # Property decorators
│ ├── init.py
│ └── product.py
├── 19_callable/ # callable() and call()
│ ├── init.py
│ └── multiplier.py
├── 20_custom_exceptions/ # Custom exceptions
│ ├── init.py
│ └── exceptions.py
└── 21_iterable/ # Custom iterables
├── init.py
└── countdown.py



## Assignment Overview

| Concept | File | Description |
|---------|------|-------------|
| 1. Using `self` | `student.py` | Student class with constructor initialization |
| 2. Using `cls` | `counter.py` | Counter tracking object instances |
| 3. Public Members | `car.py` | Car with public brand and start() method |
| 4. Class Variables | `bank.py` | Bank with shared bank_name variable |
| 5. Static Methods | `math_utils.py` | MathUtils with static add() method |
| 6. Constructors/Destructors | `logger.py` | Logger with __init__ and __del__ |
| 7. Access Modifiers | `employee.py` | Employee with public/protected/private vars |
| 8. `super()` | `inheritance.py` | Teacher inheriting from Person |
| 9. Abstract Classes | `shapes.py` | Shape ABC with Rectangle implementation |
| 10. Instance Methods | `dog.py` | Dog with bark() instance method |
| 11. Class Methods | `book.py` | Book tracking instances with class method |
| 12. Static Methods | `temperature.py` | Temperature conversion utility |
| 13. Composition | `car_engine.py` | Car containing Engine component |
| 14. Aggregation | `department_employee.py` | Department referencing Employee |
| 15. MRO | `diamond_inheritance.py` | Diamond inheritance demonstration |
| 16. Function Decorators | `decorators.py` | @log_function_call implementation |
| 17. Class Decorators | `class_decorators.py` | @add_greeting method injection |
| 18. Property Decorators | `product.py` | Managed _price with @property |
| 19. `__call__` | `multiplier.py` | Callable Multiplier instances |
| 20. Custom Exceptions | `exceptions.py` | InvalidAgeError implementation |
| 21. Custom Iterables | `countdown.py` | Countdown iterator implementation |

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/oop-practice-series.git
   cd oop-practice-series

   ## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/oop-practice-series.git
   cd oop-practice-series
Run individual assignments:

bash
python 01_self/student.py
python 02_cls/counter.py
# etc.
Explore concepts:

Each directory contains a focused implementation

Read the code and comments

Modify and experiment with the examples

Requirements
Python 3.6+

No external dependencies required

Key Concepts Covered
Fundamental OOP principles

Python's special methods (init, call, etc.)

Different types of methods (instance, class, static)

Advanced Python features (decorators, ABCs)

Object relationships (composition, aggregation)

Python-specific implementations (MRO, property decorators)