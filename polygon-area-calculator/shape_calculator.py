import  math

class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + \
           ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * (self.width + self.height)
    return perimeter
  
  def get_diagonal(self):
    diaognal = math.sqrt(self.width ** 2 + self.height ** 2)
    return diaognal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else: 
      pick_size = ("*" * self.width + "\n") * self.height
      return pick_size

  def get_amount_inside(self, shape):
        lateral_total = 0
        store = self.width
        while store >= shape.width :
            store = store -shape.width
            lateral_total = lateral_total + 1
        vert_total = 0
        y = self.height 
        while y >= shape.height :
            y -= shape.height
            vert_total = vert_total + 1

        total_fits = lateral_total * vert_total
  
        return total_fits




class Square(Rectangle):  
    
    def __init__(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)
        if self.check() == False : 
            self.__del__()
            print("Finger wag")
        else :
            return print("you have a square")

    def __str__(self):
        print(f"Square(side={self.width})")
        return f"Square(side={self.width})"

    def _del_(self):
        print("object deleted")
    
    def check(self):
        if self.width != self.height:
            print("that aint a square")
            return False
    def set_side(self, side):
        self.width = side 
        self.height = side

    def set_height(self, height):
        super().set_width(height)
        return super().set_height(height)

    def set_width(self, width):
        super().set_height(width)
        return super().set_width(width)
            


a = Rectangle(50, 10)

a.get_diagonal()

