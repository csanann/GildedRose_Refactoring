#file: test_glided_rose.py

import pytest
from gilded_rose import GildedRose, Item

def test_update_quality():
  items = [Item("Elixir of the Mongoose", sell_in = 5, quality = 7)]
  gilded_rose = GildedRose(items)
  
  gilded_rose.update_quality()
  
  assert items[0].quality == 6, "Quality of 'Elixir of the Mongoose' should decrease by 1"

def test_aged_brie_increase_in_quality():
  items = [Item("Aged Brie", sell_in = 2, quality = 0)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 1, "Quality of 'Aged Brie' should increase by 1"
  
def test_sulfuras_never_changes():
  items = [Item("Sulfuras, Hand of Ragnaros", sell_in = 0, quality = 80)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 80, "Quality of 'Sulfuras, Hand of Rgnaros' should never change"
  assert items[0].sell_in == 0, "Sell_in for 'Sulfuras, Hand of Rgnaros' should never change"

def test_backstage_passes_increase_in_quality():
  items =[Item("Backstage passes to a TAFKAL80ETC concert", sell_in = 15, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 21, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 1"

def test_backstage_passes_increase_in_quality_by_2():
  items =[Item("Backstage passes to a TAFKAL80ETC concert", sell_in = 11, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 21, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 2 when there are 10 days or less"

def test_backstage_passes_increase_in_quality_by_3():
  items =[Item("Backstage passes to a TAFKAL80ETC concert", sell_in = 6, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 22, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should increase by 2 when there are 6 days or less and by 3 when there are 5 days or less"

def test_backstage_passes_drop_to_zero():
  items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in = 0, quality = 20)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 0, "Quality of 'Backstage passes to a TAFKAL80ETC concert' should drop to zero after the concert"
  
def test_quality_never_negative():
  items = [Item("foo", sell_in = 0, quality = 0)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality >= 0, "Quality of an item is never negative"

def test_quality_never_more_than_50():
  items = [Item("Aged Brie", sell_in = 2, quality = 50)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality <= 50, "Quality of an item is never more than 50"

def test_sulfuras_never_decreases():
  items = [Item("Sulfuras, Hand of Ragnaros", sell_in = 0, quality = 80)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 80, "'Sulfuras' never decreases in quality"
  assert items[0].sell_in == 0, "'Sulfuras' never has to be sold"

def test_aged_brie_increases_quality():
  items = [Item("Aged Brie", sell_in = 2, quality = 0)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality > 0, "'Aged Brie' should increase in Quality"

def test_quality_degrades_twice_as_fast():
  items = [Item("foo", sell_in = 0, quality = 50)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 48, "Quality should degrade twice as fast once the sell by date has passed"

def test_negative_sell_in():
  items = [Item("Elixir of the Mongoose", sell_in = -5, quality = 7)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 5, "Quality of 'Elixir of the Mongoose' should decrease by 2 when sell_in is negative"
  
def test_quality_above_50():
  items = [Item("Aged Brie", sell_in = 2, quality = 55)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 50, "Quality of 'Aged Brie' should not exceed 50"

