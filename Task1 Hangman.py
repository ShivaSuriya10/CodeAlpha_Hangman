import random

words = ["python", "apple", "computer", "laptop", "programming"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("=== Hangman Game ===")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Attempts Left:", attempts)

    letter = input("Enter a letter: ").lower()

    if letter in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
        break

if "_" in guessed:
    print("\nGame Over! The word was:", word)
