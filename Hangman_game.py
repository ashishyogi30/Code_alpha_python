import random

words = ["python", "flask", "variable", "loop", "function"]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Try to guess the secret word.")
print("You have", attempts, "chances.\n")

display = "_" * len(secret_word)

while attempts > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts)
    
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.\n")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Good guess!\n")
        new_display = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                new_display += guess
            else:
                new_display += display[i]
        display = new_display
    else:
        print("Wrong guess!\n")
        attempts -= 1
        
if "_" not in display:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game over! The word was:", secret_word)
