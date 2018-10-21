import random
with open("words.txt") as f:
    words = f.read().split()
    continuegame = True
    while continuegame == True:

        chosen_word = random.choice(words)
        #print(chosen_word)
        display_word = list("_"*len(chosen_word))
        print(' '.join(display_word))
        guesscount = 1
        while '_' in display_word and guesscount <= 6:
            guess = input("Enter your guess")
            if guess not in chosen_word:
                guesscount += 1
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display_word[i] = guess
            print(' '.join(display_word))
        question = input("Wanna play a game?")
        if question == "no":
            continuegame = False
