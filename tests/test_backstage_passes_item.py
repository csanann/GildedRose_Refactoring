#file: test_backstage_passes_item.py

from src.gilded_rose import GildedRose
from src.backstage_passes_item import BackstagePassesItem

def test_backstage_passes_increase_in_quality():
  items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", sell_in = 15, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 21, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 1"
  assert items[0].sell_in == 14, "Sell in days should decrease by 1"
  
def test_backstage_passes_increase_in_quality_by_2():
  items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", sell_in = 10, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 22, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 2 when there are 10 days"
  
def test_backstage_passes_increase_in_quality_by_3():
  items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", sell_in = 3, quality = 5)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 8, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 3 when there are 5 days or less"

def test_backstage_passes_quality_drops_after_concert():
  items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", sell_in = 0, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 0, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should drop to 0 after the concert"