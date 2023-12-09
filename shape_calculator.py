class Rectangle:
    width = 0
    height = 0
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width
        if type(self) == Square:
            self.height = width

    def set_height(self,height):
        self.height = height
        if type(self) == Square:
          self.width = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        pic = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                pic += '*'*self.width + '\n'
            return pic

    def get_amount_inside(self,shape):
        x = self.width // shape.width
        y = self.height // shape.height
        return x * y

    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side

    def set_side(self,side):
        self.width = self.height = side

    def __str__(self):
      return 'Square(side='+str(self.width)+')'

