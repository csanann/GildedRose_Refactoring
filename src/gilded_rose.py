# file: src/glided_rose.py
# -*- coding: utf-8 -*-

# file: gilded_rose.py

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Conjured Mana Cake":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in <= 10: 
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in <= 5: 
                            if item.quality < 50:
                                item.quality = item.quality + 1
                    elif item.name == "Conjured Mana Cake":
                        if item.sell_in > 0:
                            item.quality = max(0, item.quality - 2)
                        else:
                            item.quality = max(0, item.quality - 4)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality > 50:
                        item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        if name == "Sulfuras, Hand of Ragnaros":
            self.quality = min(quality, 80)
        else:
            self.quality = min(quality, 50)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
