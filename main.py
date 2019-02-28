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

  def create(self,*n):
    for y in range(self.altezza):
      for x in range(self.larghezza):
        for e in n:
          if (e.x - 1) == x and (e.y - 1) == y:
            print("[{}]".format(e.graphic), end="")
            break
        else:
         print("[ ]", end="")

      print()

e = Entity(10,10,"X")
m = Entity(2,19,"M")
world = World(1,20,20)
world.create(e, m)
