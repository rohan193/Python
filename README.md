[Understanding self and __init__ method in python Class](https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/)

* self :

self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

* __init__ :

"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class

```python
class Rectange:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
   def get_area(self):
       return self.length * self.breadth
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s ", %(r.calculate_cost()))
```
