#file: aged_brie_item.py

from src.standard_item import StandardItem

class AgedBrieItem:
  def __init__(self, name, sell_in, quality):
    self.name = name
    self.sell_in = sell_in
    self.quality = quality

  def update_quality(self):
    self.sell_in -= 1
    
    if self.sell_in >= 0:
      self.quality += 1
    else:
      self.quality += 2

    self.quality = min(self.quality, 50)
