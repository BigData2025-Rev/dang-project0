class Item:
    def __init__(self, id, stats):
        self.id = id
        self.stats = stats

    def get_id(self):
        return self.id
    
    def set_stats(self, stats):
        self.stats = stats

    def get_stats(self):
        return self.stats

    def get_info(self):
        return [self.id, *self.stats]

class User:
    def __init__(self, item: Item, money=10.0, income=1.0, interest=1.01):
        self.money = money
        self.income = income
        self.interest = interest
        self.item = item

    def set_item(self, item: Item):
        self.item = item
        stats = self.item.get_stats()
        self.income = stats[1]
        self.interest = stats[2]
    
    def set_money(self, new_money):
        self.money = new_money
    
    def get_money(self):
        return self.money
    
    def get_income(self):
        return self.income
    
    def get_interest(self):
        return self.interest
    
    def get_item(self):
        return self.item