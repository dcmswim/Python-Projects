#imports needed modules
from abc import ABC, abstractmethod

#defines abstract class
class Polygon(ABC):
    def list_shape(self, shape):
        print('It is a ',shape)
        
        
    @abstractmethod
    def num_sides(self):
        pass

#defines child classes
class Triangle(Polygon):
    def num_sides(self):
        print("This shape has 3 sides.")

class Pentagon(Polygon):
    def num_sides(self):
        print("This shape has 5 sides.")

class Hexagon(Polygon):
    def num_sides(self):
        print("This shape has 6 sides.")

class Square(Polygon):
    def num_sides(self):
        print("This shape has 4 sides.")

#creating objects 
obj_tri = Triangle()
obj_tri.num_sides()
obj_tri.list_shape('triangle.')

obj_pent = Pentagon()
obj_pent.num_sides()
obj_pent.list_shape('pentagon.')

obj_hex = Hexagon()
obj_hex.num_sides()
obj_hex.list_shape('hexagon.')

obj_sq = Square()
obj_sq.num_sides()
obj_sq.list_shape('quadrilateral.')
