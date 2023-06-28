#file: test_standard_item.py

from src.standard_item import StandardItem
from src.gilded_rose import GildedRose


def test_standard_item():
  items = [StandardItem("foo", sell_in = 15, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 19, "Quality should decrease by 1"
  assert items[0].sell_in == 14, " Sell in days should decrease by 1"
  
def test_standard_item_quality_decreases_twice_as_fast_past_sell_date():
  items = [StandardItem("foo", sell_in = 0, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 18, "Quality should decrease by 2 when sell_in is less than 0"
  assert items[0].sell_in == -1, "Sell in days should decrease by 1"
