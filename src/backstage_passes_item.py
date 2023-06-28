#file: backstage_passes_item.py

from src.standard_item import StandardItem


class BackstagePassesItem:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in -= 1

        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
        elif self.sell_in <= 5 and self.sell_in > 0:
            self.quality += 3

        self.quality = min(self.quality, 50)
        self.quality = max(self.quality, 0)
