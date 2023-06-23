#file: test_standard_item.py

from standard_item import StandardItem
from gilded_rose import GildedRose


def test_standard_item():
  items = [StandardItem("foo", sell_in = 15, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 19, "Quality should decrease by 1"
  assert items[0].sell_in == 14, " Sell in days should decrease by 1"