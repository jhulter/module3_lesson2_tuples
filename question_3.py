# Task 1
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("John", "Vape", 5),
    ("George", "Chromecast", 1)
]

def show_individual_orders():
    for a, b, c in orders:
        print(f"The customer {a} ordered {c} {b}(s).")

show_individual_orders()
