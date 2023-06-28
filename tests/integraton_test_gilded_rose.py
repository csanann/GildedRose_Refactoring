# file: test_integration.py

from src.gilded_rose import GildedRose, Item

def test_integration():
  items = [
      Item("foo", 0, 0),
      Item("Aged Brie", 2, 0),
      Item("Sulfuras, Hand of Ragnaros", 0, 80),
      Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
      Item("Conjured Mana Cake", 3, 6)
  ]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()

  assert items[0].name == "foo"
  assert items[0].sell_in == -1
  assert items[0].quality == 0

  assert items[1].name == "Aged Brie"
  assert items[1].sell_in == 1
  assert items[1].quality == 1

  assert items[2].name == "Sulfuras, Hand of Ragnaros"
  assert items[2].sell_in == 0
  assert items[2].quality == 80

  assert items[3].name == "Backstage passes to a TAFKAL80ETC concert"
  assert items[3].sell_in == 14
  assert items[3].quality == 21

  assert items[4].name == "Conjured Mana Cake"
  assert items[4].sell_in == 2
  assert items[4].quality == 5
