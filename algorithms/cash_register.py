## Vijayarajan Govindarajan 2019

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
                    print(total_coins_desc)
                    return total_coins
                else:
                    total_coins_desc += ', '

def main():
    #print("Cash Register")
    coins = calculate_change(539)
    #print(coins)

if __name__ == "__main__":
    main()