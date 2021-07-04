# function
import geometry.triangle as gt

base = 10
height = 8

area_of_triangle = base * height / 2
print(f"area of triangle : {area_of_triangle}")

def count_area_of_triangle (base, height):
    area_of_triangle = base * height / 2
    return area_of_triangle

triangle_1 = count_area_of_triangle(10,6)
print(f'area of triangle 1 : {triangle_1}')

print(f'perimeter of triangle : {gt.count_perimeter_of_triangle(10,10,15)}')