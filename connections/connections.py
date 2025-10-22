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
current_words = ["AIR", "RUN", "SCREEN",
                "REWIND", "SHUFFLE", "SKIP",
                "BATH", "CARD", "PICTURE"]


def main():
    shuffle(current_words)
    print("Welcome to Connections!")
    print_grid(3, current_words)
    get_user_guess()





# Shuffle the words
import random
def shuffle(arr = current_words) -> list[str]:

    arr = arr.copy();

    for idx in range(len(arr)):
        temp = arr[idx]
        r_idx = int(random.random() * len(arr))
        arr[idx] = arr[r_idx]
        arr[r_idx] = temp

    return arr



# Print the words N2
def print_grid(words_per_row, words):
   for i in range(0, len(words), words_per_row):
       print_array(words[i:i+words_per_row])
   print()


# Get the words guessed by the user & put it into an array
def get_user_guess():
   guess = input("Enter a word group (separated by spaces): ")
   words = guess.split()
   return words



# Check that number of words is correct & words are valid







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




def print_array(array):

    for word in array:
        print(word, end="  ")
    print()

if __name__ == "__main__":
    main()
