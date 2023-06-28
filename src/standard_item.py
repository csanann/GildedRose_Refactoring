#file: standard_item.py

from src.gilded_rose import Item

class StandardItem(Item):
  def update_quality(self):
    if self.sell_in > 0:
      self.quality -= 1
    else:
      self.quality -= 2
    self.sell_in -= 1
    if self.quality < 0:
      self.quality = 0