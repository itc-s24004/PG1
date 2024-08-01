class Rectangle:
  '''長方形'''
  angle = 90

  def __init__(self, width, height) -> None:
    self.name = "rectangle"
    self.width = width
    self.height = height
    self.perimeter = self.calc_perimeter()
    self.area = self.calc_area()

  def calc_perimeter(self):
    w = self.width
    h = self.height
    return ( w + h) * 2
  
  def calc_area(self):
    w = self.width
    h = self.height
    return w * h
  
  def show_attributes(self):
    ang = self.angle
    n = self.name
    w = self.width
    h = self.height
    p = self.calc_perimeter()
    a = self.area
    print(f"name: {n}, width: {w}, height; {h}, angle: {ang}")
    print(f"perimeter: {p}, area: {a}")

r1 = Rectangle(4, 3)
r1.show_attributes()