#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Getter and setter for width
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        # Getter and setter for height
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        # Getter and setter for x
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        # Getter and setter for y
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value

# Test your implementation
if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

