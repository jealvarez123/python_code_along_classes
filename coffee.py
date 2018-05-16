class CoffeeCup():
  def __init__(self, capacity):
    self.capacity = capacity
    self.amount = 0

  def fill(self):
    self.amount = self.capacity

  def empty(self):
    self.amount = 0

  def drink(self, amount):
    self.amount -= amount
    if (self.amount == 0):
      self.amount = 0

steves_cup = CoffeeCup(12)  # a fancy latte.
seans_cup = CoffeeCup(16)    # gas station drip.
brandis_cup = CoffeeCup(2)  # a quick espresso.

steves_cup.fill()
seans_cup.fill()
brandis_cup.fill()

steves_cup.drink(1)
seans_cup.drink(1)
brandis_cup.drink(1)

print(steves_cup.amount, "ounces left")
print(seans_cup.amount, "ounces left")
print(brandis_cup.amount, "ounces left")
