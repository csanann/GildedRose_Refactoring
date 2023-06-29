#file: test_aged_brie_item.py

from src.aged_brie_item import AgedBrieItem
from src.gilded_rose import GildedRose

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
  
def test_aged_brie_increase_in_quality():
  items = [AgedBrieItem("Aged Brie", sell_in=15, quality=20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 21, "Quality of 'Aged Brie' should increase by 1"
  assert items[0].sell_in == 14, "Sell in days should decrease by 1"
  
def test_aged_brie_quality_never_more_than_50():
  items = [AgedBrieItem("Aged Brie", sell_in=15, quality=50)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 50, "'Aged Brie' quality should not increase beyond 50"
  
def test_aged_brie_quality_increase_twice_as_fast():
  items = [AgedBrieItem("Aged Brie", sell_in = -1, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 21, "Quality of 'Aged Brie' should increase by 2 when sell_in is less than 0"
  assert items[0].sell_in == -2, "Sell in days should decrease by 1"
  
