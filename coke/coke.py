def main():
    """Prompts for coin input, deducts valid coins from the amount due,
    and prints the change owed once at least 50 cents is paid.
    """
    amount_due = 50
    coins = [5, 10, 25]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin_input = int(input("Insert Coin: "))
            if coin_input in coins:
                amount_due -= coin_input
        except ValueError:
            pass

    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
