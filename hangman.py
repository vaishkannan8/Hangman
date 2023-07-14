print("\t HANGMAN GAME BY VAISHNAVI KANNAN")
hangman_word = "bottle"
max_guess = len(hangman_word) + 5
print("max guesses are ", max_guess)
guesses = 0

# Splitting Words into Characters
word_setters = list(hangman_word)
word_setters =  ['_' for i in word_setters]

def checkDone(arr):
    for i in arr:
        if i == "_":
            return False
    return True

while guesses < max_guess:
    print("GUESSES LEFT: ", max_guess - guesses)
    joined = ' '.join(word_setters)
    print(joined,end=' ')

    guess = input("Enter your guess:").lower()
    if len(guess) >1:
        print("only one character is allowed")
        continue


    for letter in range(len(hangman_word)):
        if hangman_word[letter] == guess:
            word_setters[letter] = hangman_word[letter]

    guesses += 1

    if checkDone(word_setters):
        print("WORD WAS ", hangman_word)
        print("WORD GUESSED WITH ", max_guess - guesses," LEFT")
        break

if guesses == max_guess:
    print("GUESSES OVER")
    print("WORD WAS ", hangman_word)
