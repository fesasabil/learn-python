import random

def hangman():

    word = random.choice(["pugger", "superman", "batman", "aldosh", "angela", "khufra", "wonderwoman", "atlas", "freya"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        # jika huruf yang dimasukkan benar maka berkurang _
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else :
                main = main + "_" + " "

        if main == word:
            print(main)
            print("Congrate You Win", name , "!!")
            break

        print("Guess the word:", main)
        guess = input()

        # memeriksa huruf yang dimasukkan tidak aneh - aneh
        if guess in validLetters:
            guessmade = guessmade + guess
        else :
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns -1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            elif turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("      O     ")
            elif turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("      O     ")
                print("      |     ")
            elif turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("      O     ")
                print("      |     ")
                print("     /      ")
            elif turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("      O     ")
                print("      |     ")
                print("     / \    ")
            elif turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("      O     ")
                print("     /|     ")
                print("     / \    ")
            elif turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("      O     ")
                print("     /|\    ")
                print("     / \    ")
            elif turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("      O |   ")
                print("     /|\    ")
                print("     / \    ")
            elif turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("      O_|   ")
                print("     /|\    ")
                print("     / \    ")
            elif turns == 0:
                print("You loose", name)
                print("You let a kind man die")
                print("  --------  ")
                print("      O_|   ")
                print("     |||    ")
                print("     / \    ")
                break

name = input("Enter your name : ")
print("Welcome", name)
print("==================")
print("try to guess the hero mobile legend in less than 10 attempts")
hangman()
print()