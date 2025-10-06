def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    standardized_answer = answer.lower().replace(" ", "").replace("-", "")

    if standardized_answer == "42" or standardized_answer == "fortytwo":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
