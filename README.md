# Coffee Shop OOP Model

This project is a Python-based domain model for a Coffee Shop, applying object-oriented programming principles. It simulates real-world interactions between **Customers**, **Coffees**, and **Orders**,including data validation, object relationships, and aggregate computations.

## Data structure
```
coffee-shop/
├── debug.py                     # Script for interactive testing
├── pipfile                      # pipenv dependency management
├── Pipfile.lock
├── pipfile.lock
├── readme
└── models
    ├── customer.py               # Defines the Customer class
    ├── order.py                  # Defines the Order class (joins Customers and Coffees)
    ├── coffee.py                 # Defines the Coffee class
└── tests                         # Pytest-based unit tests
    ├── test_customer.py
    ├── test_order.py
    ├── test_coffee.py

```

## Features

- Object-Oriented Design with `Customer`, `Coffee`, and `Order` classes
- Many-to-Many relationships via `Order`
- Input validation using properties and setters
- Aggregate methods: average coffee price, total orders, most spending customer
- Interactive test script and unit testing with `pytest` 


## Setup Instructions

1. Clone the repo and enter the project folder:
   ```bash
   git clone <your-repo-url>
   cd coffee_shop
   ```

2. Set up the virtual environment using `pipenv`:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Install testing dependencies:
   ```bash
   pipenv install pytest   
   
  ```
## Running the Debug Script

Use this to manually test the application:

```bash
python debug.py
```

This script demonstrates object creation, order placement, and method outputs.

## Validation Rules

| Class     | Attribute | Rule                            |
|-----------|-----------|---------------------------------|
| Customer  | name      | string, 1–15 characters         |
| Coffee    | name      | string, at least 3 characters   |
| Order     | price     | float, between 1.0 and 10.0     |
| Order     | customer  | must be a `Customer` instance   |
| Order     | coffee    | must be a `Coffee` instance     |

## Author

Zacharia Ndinguri  
Python | OOP | Software Engineering