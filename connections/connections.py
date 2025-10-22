# Constants
WORD_COUNT = 9
GROUP_SIZE = 3
BLANK = "-----"

# Declare the word groups
group1 = ["AIR", "RUN", "SCREEN"]
group2 = ["REWIND", "SHUFFLE", "SKIP"]
group3 = ["BATH", "CARD", "PICTURE"]

# put all goups together
all_groups = [group1, group2, group3]

def main():
    print("Welcome to Connections!")
    change_correct_words(["AIR", "RUN", "SCREEN"], ["AIR", "RUN", "SCREEN", "REWIND"])
    current_words = ["AIR", "RUN", "SCREEN",
                     "REWIND", "SHUFFLE", "SKIP",
                     "BATH", "CARD", "PICTURE"]

    # print_array(current_words)
for idx in range(len(arr)):
    temp = arr[idx]
    r_idx = int(random.random() * len(arr))
    arr[idx] = arr[r_idx]
    arr[r_idx] = temp

return arr












# Write your functions here!
def change_correct_words(correct_words, current_words):
    # loop through each index in all of current words
    for i in range(len(current_words)):
        # for each correct_word in all of correct_words
        if current_words[i] in correct_words:
            # replace current_words[index] with “-----”
            current_words[i] = BLANK

    # return current_words
    return current_words




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
