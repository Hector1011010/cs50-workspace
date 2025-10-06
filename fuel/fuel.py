def main():
    while True:
        fraction_str = input("Fraction: ")
        try:
            numerator_str, denominator_str = fraction_str.split('/')
            numerator = int(numerator_str)
            denominator = int(denominator_str)

            if denominator == 0:
                raise ZeroDivisionError
            if numerator < 0 or denominator < 0:
                raise ValueError
            if numerator > denominator:
                raise ValueError

            percentage = round((numerator / denominator) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()
