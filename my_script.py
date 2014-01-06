import sys									            # Import Python system library
from my_package.models import add_some_values, Member   # Import our models

if __name__ == "__main__":						        # This is equivalent to main() in C++
    a = Member('John','0001')
    b = add_some_values(2, 2)
