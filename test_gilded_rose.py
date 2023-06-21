#file: test_glided_rose.py

import pytest
from gilded_rose import GildedRose, Item

def test_update_quality():
  #for unit test, we will use arrange, act and assert structure here
  items = [Item("Elixir of the Mongoose", sell_in = 5, quality = 7)]
  gilded_rose = GildedRose(items)
  
  gilded_rose.update_quality()
  
  assert items[0].quality == 6, "Quality of 'Elixir of the Mongoose' should decrease by 1"
