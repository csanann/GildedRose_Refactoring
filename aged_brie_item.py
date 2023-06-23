#file: aged_brie_item.py

from standard_item import StandardItem

class AgedBrieItem(StandardItem):
  def update_quality(self):
    if self.sell_in > 0:
      self.quality += 1
    else:
      self.quality += 2
    self.sell_in -= 1
    if self.quality > 50:
      self.quality = 50