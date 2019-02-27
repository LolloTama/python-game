class Entity:
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic


e = Entity(5, 5, "X")

for y in range(10):
  for x in range(10):
    if e.x == x and e.y == y:
      print("[{}]".format(e.graphic), end="")
    else:
      print("[ ]", end="")

  print()


class World:
  def __init__(self,level_number,larghezza,altezza):
    self.level_number = level_number
    self.larghezza = larghezza
    self.altezza = altezza

  def create(self,larghezza,altezza):
    for y in range(10):
      for x in range(10):
        if e.x == x and e.y == y:
          print("[{}]".format(e.graphic), end="")
        else:
          print("[ ]", end="")

      print()
