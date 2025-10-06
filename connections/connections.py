# Constants
WORD_COUNT = 9
GROUP_SIZE = 3
BLANK = "-----"

# Declare the word groups
group1 = ["AIR", "RUN", "SCREEN"]
group2 = ["REWIND", "SHUFFLE", "SKIP"]
group3 = ["BATH", "CARD", "PICTURE"]


def main():
    print("Welcome to Connections!")

    current_words = ["AIR", "RUN", "SCREEN",
                     "REWIND", "SHUFFLE", "SKIP",
                     "BATH", "CARD", "PICTURE"]

    print_array(current_words)


# Write your functions here!
def change_correct_words(correct_words, current_words):
    """
    >>> change_correct_words(["AIR", "RUN", "SCREEN"], ["AIR", "RUN", "SCREEN", "REWIND", "SHUFFLE", "SKIP","BATH", "CARD", "PICTURE"])
    ["-----", "-----", "-----",
                     "REWIND", "SHUFFLE", "SKIP",
                     "BATH", "CARD", "PICTURE"]
    """
    print(correct_words, current_words)




# Helper function I wrote for you
def print_array(array):
    """
    Print words in a row, separated by two spaces.
    """
    for word in array:
        print(word, end="  ")
    print()

if __name__ == "__main__":
    main()
