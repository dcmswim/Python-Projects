
from abc import ABC, abstractmethod

#defines abstract class
class Polygon(ABC):
    @abstractmethod
    def num_sides(self):
        pass

#defines child classes
class Triangle(Polygon):
    def num_sides(self):
        print("Triangles have 3 sides")

class Pentagon(Polygon):
    def num_sides(self):
        print("Pentagons have 5 sides")

class Hexagon(Polygon):
    def num_sides(self):
        print("Hexagons have 6 sides")

class Square(Polygon):
    def num_sides(self):
        print("Quadrilaterals have 4 sides")

#creating objects 
obj_tri = Triangle()
obj_tri.num_sides()

obj_pent = Pentagon()
obj_pent.num_sides()

obj_hex = Hexagon()
obj_hex.num_sides()

obj_sq = Square()
obj_sq.num_sides()
