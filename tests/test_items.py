# test_items.py

from src.items import AgedBrieItem, ElixirOfTheMongooseItem, SulfurasItem, BackstagePassesItem, RegularItem, ConjuredItem

def test_aged_brie_item():
  item = AgedBrieItem("Aged Brie", 2, 0)
  item.update_quality()
  assert item.quality == 1, "Quality of 'Aged Brie' should increase by 1"
  assert item.sell_in == 1, "Sell in days should decrease by 1"

def test_elixir_of_the_mongoose_item():
  item = ElixirOfTheMongooseItem("Elixir of the Mongoose", 5, 7)
  item.update_quality()
  assert item.quality == 6, "Quality of 'Elixir of the Mongoose' should decrease by 1"
  assert item.sell_in == 4, "Sell in days should decrease by 1"

def test_sulfuras_item():
  item = SulfurasItem("Sulfuras, Hand of Ragnaros", 0, 80)
  item.update_quality()
  assert item.quality == 80, "Quality of 'Sulfuras, Hand of Ragnaros' should always be 80"
  assert item.sell_in == 0, "Sell in days of 'Sulfuras, Hand of Ragnaros' should always be 0"

def test_backstage_passes_item():
  item = BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 15, 20)
  item.update_quality()
  assert item.quality == 21, "Quality of 'Backstage passes' should increase by 1 when sell_in > 10"
  assert item.sell_in == 14, "Sell in days should decrease by 1"

def test_regular_item():
  item = RegularItem("foo", 15, 20)
  item.update_quality()
  assert item.quality == 19, "Quality of a regular item should decrease by 1"
  assert item.sell_in == 14, "Sell in days should decrease by 1"

def test_conjured_item():
  item = ConjuredItem("Conjured Mana Cake", 3, 6)
  item.update_quality()
  assert item.name == "Conjured Mana Cake"
  assert item.sell_in == 2
  assert item.quality == 4
  
  item.update_quality()
  assert item.name == "Conjured Mana Cake"
  assert item.sell_in == 1
  assert item.quality == 2
  
  item.update_quality()
  assert item.name == "Conjured Mana Cake"
  assert item.sell_in == 0
  assert item.quality == 0