# polygon-area-calculator
A Python Polygon Area Calculator project practising object-oriented programming, inheritance, and geometric calculations.
## Features

- Calculate the area of a rectangle or square.
- Calculate the perimeter and diagonal.
- Generate text-based pictures using asterisks (`*`).
- Determine how many shapes fit inside another rectangle.
- Change the dimensions of rectangles and squares.
- Use inheritance to share methods between the `Rectangle` and `Square` classes.
- Maintain equal width and height when modifying a square.

## Concepts Practised

- Python classes and objects
- Object-oriented programming (OOP)
- Constructors and instance attributes
- Inheritance and method overriding
- Methods and string representation
- Loops and conditional statements
- Mathematical calculations and floor division

## Technologies

- Python
- `math` module

## Example Usage

```python
rect = Rectangle(10, 5)
print(rect.get_area())
# 50

sq = Square(9)
print(sq.get_area())
# 81

sq.set_side(4)
print(sq)
# Square(side=4)
```

## Attribution

This project was completed as part of the **freeCodeCamp Python curriculum**, following the Polygon Area Calculator project requirements.

The project is published to demonstrate my Python learning progress and understanding of object-oriented programming.

## Author

Created as part of my journey toward developing practical Python and data analytics skills.
