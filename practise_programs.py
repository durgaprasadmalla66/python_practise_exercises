#guess the word game
word = "python"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
while guess != word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ").lower()
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, you lose!")
else:    print("You win!")        
