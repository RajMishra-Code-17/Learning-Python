
import math

def circle_stat(radius):
    area = (math.pi * radius ** 2)
    circumference = (2 * math.pi * radius)
    return (area,circumference)

a, b = circle_stat(4)

print("Area of circle: ",a,"circumference: ",b)

# here we have done the both circumference and area of the circle
# practice one more time for the more clarity

# import math

# def circle_area_cirm(radius):
#     area = math.pi * radius * radius
#     circumference = 2 * math.pi * radius

#     return area, circumference

# a,b = circle_area_cirm(55)

# print("area : ",a,"circumference ",b)


