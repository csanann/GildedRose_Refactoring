# file: test_conjured_item.py

from src.gilded_rose import GildedRose
from src.conjured_item import ConjuredItem

def test_conjured_item_decreases_in_quality():
    items = [ConjuredItem("Conjured Mana Cake", sell_in=15, quality=20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 19, "Quality of 'Conjured Mana Cake' should decrease by 1"
    assert items[0].sell_in == 14, "Sell in days should decrease by 1"

def test_conjured_item_decreases_twice_as_fast_past_sell_date():
    items = [ConjuredItem("Conjured Mana Cake", sell_in=0, quality=20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 16, "Quality of 'Conjured Mana Cake' should decrease by 4 when sell_in is less than 0"
    assert items[0].sell_in == -1, "Sell in days should decrease by 1"
