import random
from classmodule import Item, User

def update_money(curr_dt, income_dt, user: User):
    dt_difference = curr_dt - income_dt
    secs = dt_difference.total_seconds()
    if (secs >= 1):
        income_dt = curr_dt
        new_money = user.get_money() + (user.get_income() * secs)
        new_money *= user.get_interest() ** secs
        new_money = min(new_money, 100000000)

        user.set_money(new_money)

        return curr_dt
    
    return income_dt

def create_item(id: int):
    income = 2 ** ((random.random() + 0.1) * 10)
    interest = 1.01 ** ((random.random() + 0.1) * 10)
    cost = (income ** (1 + ((interest - 1) * 5))) * random.randint(2, 5)

    return Item(id, [cost, income, interest])

def craft_item(item: Item, type):
    stats = item.get_stats()
    if (type == "income"):
        stats[1] = stats[1] * (20 + random.random()) / 20
    elif (type == "interest"):
        stats[2] = stats[2] * (200 + random.random()) / 200
    item.set_stats(stats)