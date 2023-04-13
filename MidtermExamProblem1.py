import math

class Circle:
  def __init__(attributes, radius):
    attributes.radius=radius
    attributes.pi=math.pi
  def perimeter(attributes):
    return 2*attributes.pi*attributes.radius
  def area(attributes):
    return attributes.pi*(attributes.radius**2)
  def display(attributes):
    print("Your circle has a perimeter of", attributes.perimeter())
    print("And a circumference of", attributes.area())

samplecircle=Circle(float(input("Give a radius: ")))
samplecircle.display()
