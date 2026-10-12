Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
... class Rectangle:
...     def __init__(self, width, height):
...         self.width = width
...         self.height = height
... 
...     def set_width(self, width):
...         self.width = width
... 
...     def set_height(self, height):
...         self.height = height
... 
...     def get_area(self):
...         return self.width * self.height
... 
...     def get_perimeter (self):
...         return 2 * (self.width + self.height)
... 
...     def get_diagonal(self):
...         return math.sqrt(self.width ** 2 + self.height ** 2)
... 
...     def get_picture(self):
...         if self.width > 50 or self.height > 50:
...             return "Too big for picture."
...         picture = ""
...         for _ in range(self.height):
...             picture += "*" * self.width + "\n"
...         return picture
... 
...     def get_amount_inside(self, shape):
...         return (self.width // shape.width) * (self.height // shape.height)
... 
...     def __str__(self):
...         return f"Rectangle(width={self.width}, height={self.height})"
... 
... class Square(Rectangle):
...     def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"
