# file: src/glided_rose.py
# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in >= 10:
                    item.quality += 1
                elif item.sell_in >= 5:
                    item.quality += 2
                elif item.sell_in >= 0:
                    item.quality += 3
                else:
                    item.quality = 0

            elif item.name == "Aged Brie":
                item.quality += 1 if item.quality < 50 else 0
                
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Do not change quality or sell_in.

            else:
                item.quality -= 2 if item.sell_in < 0 else 1
                item.quality = 0 if item.quality < 0 else item.quality

            if item.quality > 50:
                item.quality = 50  # Quality should never be more than 50.


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)