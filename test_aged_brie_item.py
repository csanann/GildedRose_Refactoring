#file: test_aged_brie_item.py

from aged_brie_item import AgedBrieItem
from gilded_rose import GildedRose

def test_aged_brie_item():
  items = [AgedBrieItem("Aged Brie", sell_in = 2, quality = 0)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 1, "Quality of 'Aged Brie' should increase by 1"
  assert items[0].sell_in == 1, "Sell in days should decrease by 1"

def test_aged_brie_item_quality_max():
  items = [AgedBrieItem("Aged Brie", sell_in = 2, quality = 50)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 50, "Quality of 'Aged Brie' should not exceed 50"