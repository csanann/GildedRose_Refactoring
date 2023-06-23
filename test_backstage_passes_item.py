#file: test_backstage_passes_item.py

from gilded_rose import GildedRose
from backstage_passes_item import BackstagePassesItem

def test_backstage_passes_increase_in_quality():
  items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", sell_in = 15, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 21, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 1"
  assert items[0].sell_in == 14, "Sell in days should decrease by 1"