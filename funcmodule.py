import random
from classmodule import Item, User

def update_money(curr_dt, income_dt, user: User):
    dt_difference = curr_dt - income_dt
    if (dt_difference >= 1):
        income_dt = curr_dt
        new_money = user.get_money() + (user.get_income() * dt_difference)
        new_money *= user.get_interest() ** dt_difference
        new_money = min(new_money, 100000000)

        user.set_money(new_money)

        return curr_dt
    
    return income_dt

def create_item(id: int):
    income = 2 ** ((random.random() + 0.1) * 10)
    interest = 1.01 ** ((random.random() + 0.1) * 10)
    cost = (income ** (1 + ((interest - 1) * 5))) * random.randint(2, 5)

    return Item(id, [cost, income, interest])