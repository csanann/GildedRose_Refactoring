# file: conjured_item.py

class ConjuredItem:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in -= 1
        self.quality -= 2 if self.sell_in >= 0 else 4
        self.quality = max(0, self.quality)
   
