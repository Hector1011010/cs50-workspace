# Constants
WORD_COUNT = 16
GROUP_SIZE = 4
BLANK = "-----"

# Declare the word groups
group1 = ["DEAD", "PAD", "COMBINATION"]
group2 = ["DAY", "SPOT", "SKIP"]
group3 = ["BATH", "CARD", "PICTURE"]

# put all groups together
current_words = ["AIR", "RUN", "SCREEN",
                 "REWIND", "SHUFFLE", "SKIP",
                 "BATH", "CARD", "PICTURE"]


import random

def shuffle(arr: list[str]) -> list[str]:
    arr = arr.copy()
    for idx in range(len(arr)):
        temp = arr[idx]
        r_idx = int(random.random() * len(arr))
        arr[idx] = arr[r_idx]
        arr[r_idx] = temp
    return arr

current_words = shuffle(current_words)


# Print the words N2
def print_array(array):
    for word in array:
        print(word, end="  ")
    print()


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
def check_answer(user_guess):
    # Must have exactly 3 words
    if len(user_guess) != 4:
        print("Try again")
        return False

    # Make sure all words exist in current list
    for word in user_guess:
        if word not in current_words:
            print(f"{word.capitalize()} is not an answer")
            return False

    # Check if guess matches any correct group (sorted comparison)
    sorted_guess = sorted(user_guess)
    if (sorted_guess == sorted(group1) or
        sorted_guess == sorted(group2) or
        sorted_guess == sorted(group3)):
        print("Correct group found! :)")
        return True
    else:
        print("That’s not a correct group. :(")
        return False


# Uppercase all the letters in the user guess
def upper_guess(user_guesses):
    upper_list = []
    for guess in user_guesses:
        upper_list.append(guess.upper())
    return upper_list


def find_smallest(arr, start):
    min_idx = start
    for j in range(start + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    return min_idx


def sort_answer(game_answer):
    for i in range(len(game_answer)):
        first_answer = find_smallest(game_answer, i)
        game_answer[i], game_answer[first_answer] = game_answer[first_answer], game_answer[i]
    return game_answer


def inputscorrect(current_words, group1, group2, group3):
    if current_words == group1:
        return True
    elif current_words == group2:
        return True
    elif current_words == group3:
        return True
    else:
        return False


def array_check(user, correct):
    for i in range(len(correct)):
        if user[i] != correct[i]:
            return False
    return True


def change_correct_words(correct_words, current_words):
    for i in range(len(current_words)):
        if current_words[i] in correct_words:
            current_words[i] = BLANK
    return current_words



def check_win(words: list[str]) -> bool:
    for word in words:
        if word != BLANK:
            return False
    return True



def main():
    shuffled_words = shuffle(current_words)
    print("Welcome to Connections!")
    print_grid(3, shuffled_words)

    while True:
        user_guess = get_user_guess()
        user_guess = upper_guess(user_guess)

        if check_answer(user_guess):
            print("Your guess is valid!")

            shuffled_words = change_correct_words(user_guess, shuffled_words)
            print_grid(3, shuffled_words)

            if check_win(shuffled_words):
                print("Yayyy! You found all connections!")
                break
        else:
            print("Invalid guess.")



if __name__ == "__main__":
    main()
