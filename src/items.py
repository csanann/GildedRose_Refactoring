# file: items.py

from abc import ABC, abstractmethod

class Item(ABC):
  def __init__(self, name, sell_in, quality):
    self.name = name
    self.sell_in = sell_in
    self.quality = quality
    
  def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

  @abstractmethod
  def update_quality(self):
    pass


class AgedBrieItem(Item):
  def update_quality(self):
    if self.quality < 50:
      self.quality += 1
    self.sell_in -= 1
    if self.sell_in < 0 and self.quality < 50:
      self.quality += 1


class ElixirOfTheMongooseItem(Item):
  def update_quality(self):
    if self.quality > 0:
      self.quality -= 1
    self.sell_in -= 1
    if self.sell_in < 0 and self.quality > 0:
      self.quality -= 1


class SulfurasItem(Item):
  def update_quality(self):
    pass  # Sulfuras does not change


class BackstagePassesItem(Item):
  def update_quality(self):
    if self.quality < 50:
      self.quality += 1
      if self.sell_in <= 10:
        if self.quality < 50:
          self.quality += 1
      if self.sell_in <= 5:
        if self.quality < 50:
          self.quality += 1
    self.sell_in -= 1
    if self.sell_in < 0:
      self.quality = 0


class RegularItem(Item):
  def update_quality(self):
    if self.quality > 0:
      self.quality -= 1
    self.sell_in -= 1
    if self.sell_in < 0 and self.quality > 0:
      self.quality -= 1
