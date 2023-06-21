#file: test_glided_rose.py

import pytest
from gilded_rose import GildedRose, Item

def test_update_quality():
  #for unit test, we will use arrange, act and assert structure here
  items = [Item("Elixir of the Mongoose", sell_in = 5, quality = 7)]
  gilded_rose = GildedRose(items)
  
  gilded_rose.update_quality()
  
  assert items[0].quality == 6, "Quality of 'Elixir of the Mongoose' should decrease by 1"

def test_aged_brie_increase_in_quality():
  items = [Item("Aged Brie", sell_in = 2, quality = 0)]
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  assert items[0].quality == 1, "Quality of 'Aged Brie' should increase by 1"