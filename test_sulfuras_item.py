#file: test_sulfuras_item.py

from gilded_rose import GildedRose
from sulfuras_item import SulfurasItem

def test_sulfuras_never_decreases_in_quality():
  items = [SulfurasItem("Sulfuras, Hand of Ragnaros", sell_in = 0, quality = 80)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 80, "Quality of 'Sulfuras, Hand of Ragnaros' should always be 80"
  assert items[0].sell_in == 0, "Sell in days of 'Sulfuras, Hand of Ragnaros' should always be 0"
