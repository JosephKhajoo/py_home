import math
import sys

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def calc_area(self):
		result = math.pi * (self.radius ** 2)
		return f"The Area of a circle with a radius of {self.radius} is {result}"

	def calc_perim(self):
		result = math.pi * self.radius * 2
		return f"The Perimeter of a circle with a radius of {self.radius} is {result}"
try:
	user_input = int(input("Enter a radius: "))
except Exception:
	print("Please enter valid numbers.")
	sys.exit()

circle = Circle(user_input)

print(circle.calc_area())
print(circle.calc_perim())