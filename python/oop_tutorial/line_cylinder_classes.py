import math
class Line():

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        #return math.sqrt(((self.coord2[0] - self.coord1[0])**2)+((self.coord2[1] - self.coord1[1])**2))
        x1,y1 = self.coord1
        x2,y2 = self.coord2

        return (((x2-x1)**2)+((y2-y1)**2))**0.5


    def slope(self):
        #return (self.coord2[1] - self.coord1[1])/(self.coord2[0] - self.coord1[0])
        x1,y1 = self.coord1
        x2,y2 = self.coord2

        return (y2-y1)/(x2-x1)

cord1 = (3,2)
cord2 = (8,10)

li = Line(cord1,cord2)

print(li.slope())
print(li.distance())

class Cylinder():

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def area(self):
        return (2* math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))


c = Cylinder(2,3)

print(c.volume())
print(c.area())
