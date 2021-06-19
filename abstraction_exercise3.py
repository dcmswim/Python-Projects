#imports needed modules
from abc import ABC, abstractmethod

#defines abstract class
class Polygon(ABC):
    def list_shape(self, shape):
        print(shape)
        
        
    @abstractmethod
    def num_sides(self, shape):
        pass

#defines child classes
class Triangle(Polygon):
    def num_sides(self,shape):
        print("This shape has 3 sides. It is a {}".format(shape))

class Pentagon(Polygon):
    def num_sides(self,shape):
        print("This shape has 5 sides. It is a {}".format(shape))

class Hexagon(Polygon):
    def num_sides(self,shape):
        print("This shape has 6 sides. It is a {}".format(shape))

class Square(Polygon):
    def num_sides(self,shape):
        print("This shape has 4 sides. It is a {}".format(shape))

#creating objects 
obj_tri = Triangle()
obj_tri.num_sides('triangle')

obj_pent = Pentagon()
obj_pent.num_sides('pentagon')

obj_hex = Hexagon()
obj_hex.num_sides('hexagon')

obj_sq = Square()
obj_sq.num_sides('quadrilateral')
