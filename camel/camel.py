def main():
    camelCase = input("camelCase: ")
    snakeCase = change_to_snake_Case(camelCase)
    # print("snakeCase: " + camelCase)

def change_to_snake_Case(camel_case_string):
    snake_case_result = ""
    for I in camel_case_string:
        if I.isupper():
            snake_case_result += "_" + I.lower()
        else:
            snake_case_result += I
    print("snakeCase: " + snake_case_result)


# if __name__ == "__main__":
main()

