import random

name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the guessing game!")
words = ["guessing","apple","earphones","macbook","python",
        "television", "sunset","opensource"]


index = random.randint(0, len(words))
word = words[index]
indexes = random.sample(range(0, len(word)), 3)
guesses = "" #characters that the user has guessed so far
for i in indexes:
    guesses += word[i]
chances = 10
play = "Yes"

def playagain():
    # this will help you understad scoping
    global play
    play = input("Do you want to play again? (Yes/No): ")
    if play == "Yes":
        global chances, word, guesses
        chances = 10
        index = random.randint(0, len(words))
        word = words[index]
        indexes = random.sample(range(0, len(word)), 3)
        guesses = "" 
        for i in indexes:
            guesses += word[i]


while play == "Yes":
    while chances > 0:
        won = True
        for ch in word:
            if ch in guesses: 
                print(ch, end=" ")
            else:
                print("_", end=" ")
                won = False

        if won:
            print("\nYou Won!")
            print(f"Your score is {chances * 10}")
            playagain()
            break

     
        guess = input("\nGuess a character: ")
        guesses += guess

        if guess not in word:
            chances -= 1
            print("\nWrong Answer!!")
            print(f"You have {chances} chances left!")

            if chances == 0:
                print("You Lose!!")
                playagain()
                break
print("Thanks for playing!")
