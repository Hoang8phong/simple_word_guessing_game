import random

# words_list = ["swift", "python", "javascript", "java", "assembly", "ruby", "php" ]
with open('Catchphrase_Words_Medium.txt', 'r') as file:
    words_list = [line.strip().lower() for line in file if line.strip()]

secret_word = random.choice(words_list)
guessed_word = ["_" for _ in secret_word]

max_guesses = 6
wrong_guesses = 0
guessed_letters = set()

while True:
    print("\nCurrent word", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print(f"Remaining guesses: {max_guesses - wrong_guesses}")

    while True:
        guess = input("Enter your guess: ").lower().strip()
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        elif not guess.isalpha():
            print("Please enter only alphabet letters.")
            continue
        elif guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        else:
            break

    guessed_letters.add(guess)

    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if guess == letter:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print(f"Wrong guesses: {guess} is not in the word.")
        print(f"You have {max_guesses - wrong_guesses} wrong guesses remaining.")

    if "".join(guessed_word) == secret_word:
        print("Congratulations, you guessed the word!")
        break

    if wrong_guesses >= max_guesses:
        print("Sorry, you lose :(")
        print(f"The word was: {secret_word}")
        break




