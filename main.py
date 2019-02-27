class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic

class World:
  def __init__(self,level_number,larghezza,altezza):
    self.level_number = level_number
    self.larghezza = larghezza
    self.altezza = altezza

  def create(self):
    for y in range(self.altezza):
      for x in range(self.larghezza):
        if e.x == x and e.y == y:
          print("[{}]".format(e.graphic), end="")
        else:
          print("[ ]", end="")

      print()

e = Entity(5, 5, "X")
world = World(1,10,10)
world.create()
