
# Step 1: To generate radom word from the given list of words, we need to select a random word from the list.

import random
import hangman_image
import word_file
word_list = word_file.words
print("Hint: The word is a vehicle.")
word = random.choice(word_list);
# print(word);

# Step 2: Generate _ array of the same length as the word, filled with underscores.
underscore_arr = []
word_length = len(word)
for i in range(word_length):
    underscore_arr.append("_");
print(underscore_arr);

# Step 3: Taking input from the user based how many chance left to guess the word.
chance = 7
is_game_over = False
while not is_game_over:
    guess = input("Guess the word: ")
    for i in range(word_length):
        if guess.lower() == word[i].lower():
            underscore_arr[i] = guess;
            print(underscore_arr);
    if "_" not in underscore_arr:
        is_game_over = True
        print("You won!");
    if guess.lower() not in word.lower():
        chance -= 1
        print(hangman_image.hangman[chance]);
        print(f"You have {chance} chances left");
    if chance == 0:
        is_game_over = True
        print("You lost! The word was " + word);


