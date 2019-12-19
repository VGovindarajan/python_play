## Vijayarajan Govindarajan 2019
from collections import deque

coins_list = [25, 10, 5, 1]
coins_names_singular = {25: 'Quarter', 10: 'Dime', 5: 'Nickel', 1: 'Penny'}
coins_names_plural = {25: 'Quarters', 10: 'Dimes', 5: 'Nickel', 1: 'Pennies'}

def get_coin_name(coin_amount, coin_count):
    if coin_count > 1:
        return coins_names_plural[coin_amount]
    else:
        return coins_names_singular[coin_amount]

def calculate_change(balance):
    total_coins = 0
    total_coins_desc = ''
    if balance <= 0:
        return total_coins
    while True:
        for coin_amount in coins_list:
            coin_count = balance // coin_amount
            if coin_count > 0:
                total_coins += coin_count
                total_coins_desc += str(coin_count) + ' ' + get_coin_name(coin_amount, coin_count)
                balance = balance % coin_amount
                if balance == 0:
                    total_coins_desc += '.'
                    #print(total_coins_desc)
                    return total_coins
                else:
                    total_coins_desc += ', '


def calculate_min_count_change_dynamic(balance_in_pennies, available_coins_list):
    dynamic_array = [balance_in_pennies+1] * (balance_in_pennies + 1)
    dynamic_array[0] = 0
    #print(dynamic_array)
    #print(available_coins_list)
    #print(balance_in_pennies)
    for i in range (1, balance_in_pennies+1, 1):
        for coin in available_coins_list:
            if i - coin >= 0:
                dynamic_index = i - coin
                dynamic_array[i] = min(dynamic_array[i], dynamic_array[dynamic_index]+1)
    #print(dynamic_array)
    return dynamic_array[balance_in_pennies]


def coin_change_tree(balance_in_pennies, available_coins, amount_dict_list):
    #print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    #print("Starting for", balance_in_pennies)
    #print(available_coins)
    #print(amount_dict_list)

    #available_coins.sort(reverse=True)
    for coin in available_coins:
        balance_after_last_coin = balance_in_pennies - int(coin)
        if balance_after_last_coin is 0:
            amount_dict_list[balance_in_pennies] = 1

        if balance_after_last_coin > 0:
            if balance_after_last_coin not in amount_dict_list:
                #print("Missing {0} in {1}".format(balance_after_last_coin, amount_dict_list))
                coin_change_tree(balance_after_last_coin, available_coins, amount_dict_list)
            if balance_after_last_coin in amount_dict_list:
                #print("Found {0} in {1}".format(balance_after_last_coin, amount_dict_list))
                current_coin_count = amount_dict_list[balance_after_last_coin] + 1
                previous_count = 1000
                if balance_in_pennies in amount_dict_list:
                    previous_count = amount_dict_list[balance_in_pennies]
                if current_coin_count < previous_count:
                    amount_dict_list[balance_in_pennies] = current_coin_count
                    #print("Updated {0} to {1}".format(balance_in_pennies, current_coin_count))
            else:
                raise ValueError("{0} not found in {1}".format(balance_after_last_coin, amount_dict_list))

    #print(amount_dict_list)
    if balance_in_pennies in amount_dict_list:
        #print(amount_dict_list)
        return amount_dict_list[balance_in_pennies]


def coin_change_tree_inefficient(balance_in_pennies, available_coins):
    amount_dict_list = {}
    change_queue = deque()
    for coin in available_coins:
        change_queue.appendleft([coin])
    while len(change_queue) > 0:
        previous_list = []
        #print(len(change_queue))
        if len(change_queue) > 0:
            previous_list = change_queue.pop()
        for current_coin in available_coins:
            current_list = previous_list.copy()
            current_list.append(current_coin)
            current_sum = sum(current_list)
            print("current_list={0}, sum={1}".format(current_list, current_sum))
            if current_sum <= balance_in_pennies:
                current_change_list = []
                if current_sum in amount_dict_list:
                    current_change_list = amount_dict_list[current_sum]
                current_change_list.append(current_list)
                amount_dict_list[current_sum] = current_change_list
                change_queue.appendleft(current_list)
                print("Added current_list {0}, current sum = {1}".format(current_list, current_sum))
                print("change_queue",change_queue)

    if balance_in_pennies in amount_dict_list:
        change_lists = amount_dict_list[balance_in_pennies]
        for change_list in change_lists:
            print("selected change_list",change_list)
        return len(change_lists)

def main():
    #print("Cash Register")
    #coins = calculate_change(539)
    #print(coins)
    #coins_tree = coin_change_tree_inefficient(31, [1, 10, 25])
    coins_dynamic = calculate_min_count_change_dynamic(31, [1,2,5,25])
    print(coins_dynamic)
    coins_tree = coin_change_tree(31, [1,2,5,25], {})
    print(coins_tree)


if __name__ == "__main__":
    main()