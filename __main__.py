import csv
import datetime as dt
from classmodule import Item, User
from funcmodule import update_money, create_item

def main():    
    income_dt = dt.datetime.now()

    market = []
    with open('data/market.csv', 'r') as file:
        market_reader = csv.reader(file)
        for row in market_reader:
            market.append(row)

    if (len(market[1:]) < 20):
        max_id = 0
        for item in market[1:]:
            max_id = max(max_id, int(item[0]))
        
        with open('data/market.csv', 'w', newline="") as file:
            market_writer = csv.writer(file)
            if (len(market) == 0):
                header = ["id", "cost", "income", "interest"]
                market.append(header)
                market_writer.writerow(header)
            for _ in range(20 - len(market[1:])):
                max_id += 1
                item = create_item(max_id)
                market.append(item.get_info())
                market_writer.writerow(item.get_info())

    item = Item(0, [0,1.0,1.01])
    user = User(item)

    user_input = ""

    while (True):
        user_input = input("Enter your next command: ")
        user_input = user_input.lower()
        curr_dt = dt.datetime.now()
        income_dt = update_money(curr_dt, income_dt, user) # Update money every loop

        if (user_input == "exit"):
            print("Goodbye.")
            break
        
        elif (user_input == "help"):
            print("help        Prints a list of commands\nmoney       Prints your current amount of money\nstats       Prints your income and interest\nmarket      Prints list of current items in market\nbuy         Purchase an item from the current market\nexit        Exits the program")
            continue

        elif (user_input == "money"):
            print('${:.2f}'.format(user.get_money()))
            continue
        
        elif (user_input == "stats"):
            print('money: {:.2f} | income: ${:.2f} | interest: {:.2f}%'.format(user.get_money(), user.get_income(), user.get_interest()))
        
        elif (user_input == "market"):
            for item in market[1:]:
                print('id: {} | cost: ${:.2f} | income: ${:.2f} | interest: {:.2f}%'
                      .format(int(item[0]), float(item[1]), float(item[2]), (float(item[3])-1)*100))

        elif (user_input == "buy"):
            item_id = input("Enter the id of the item you would like to buy: ")
            if (item_id.lower() != "exit"):
                valid_id = False
                for item in market[1:]:
                    if (str(item[0]) == str(item_id)):
                        bought_item = Item(int(item[0]), [float(item[1]), float(item[2]), float(item[3])])
                        valid_id = True
                        break
                
                if (valid_id == False):
                    print("Not a valid id.")
                else:
                    curr_dt = dt.datetime.now()
                    income_dt = update_money(curr_dt, income_dt, user)
                    money = user.get_money()
                    stats = bought_item.get_stats()
                    if (money < float(stats[0])):
                        print("Not enough money.")
                    else:
                        user.set_item(bought_item)
                        user.set_money(money - float(stats[0]))
                        print("Successfully purchased.")

        else:
            print("Error: invalid command. Type 'help' to get a list of commands.")
        
    return 0


if __name__ == '__main__':
    main()