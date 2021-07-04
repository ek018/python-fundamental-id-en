# encapsulation
from geometry.rectangle import Rectangle
from geometry.shape import Shape

rectangle_1 = Rectangle(10)
print(rectangle_1.area())

rectangle_2 = Rectangle(7)
print(rectangle_2.area())

# inheritance
shape_1 = Shape()
print(f'{shape_1.area()}')


# polymorphism
list_of_shape = [rectangle_1, rectangle_2]
for shape in list_of_shape:
    area_rectangle = shape.area()
    print(f'{area_rectangle}')