temperatures = [72, 68, 75]

temperatures.append(59)
temperatures.append(76)
temperatures.append(56)
temperatures.append(61)

try:
    day = int(input("Enter the day of the week (0–6): "))

    print("Temperature on that day:", temperatures[day])

    average = sum(temperatures) / len(temperatures)
    print("Average temperature:", average)

except IndexError:
    print("Error: Day must be between 0 and 6.")

except ZeroDivisionError:
    print("Error: No temperatures available to average.")

except ValueError:
    print("Error: Please enter a valid number between 0 and 6.")

print("All recorded temperatures:")
for i, temp in enumerate(temperatures):
    print(f"Day {i}: {temp}")









shopping_list = ["milk", "eggs", "bread"]

try:
    item = input("Which item would you like to remove? ")
    shopping_list.remove(item)
    print("First item is:", shopping_list[0])

except ValueError:
    print("Error: That item is not in the shopping list.")
    if item not in shopping_list():
        print("that item is not in list")


print("New Shopping list:")
for i, thing in enumerate(shopping_list):
    print(f"{i + 1}: {thing}")
