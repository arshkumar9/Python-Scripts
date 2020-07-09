import random
def random_word():
    f = open('american-english', 'r')
    content = f.read().splitlines()
    f.close()
    return random.choice(content)

def main_game():
    word = random_word().lower()
    print(word)
    backup_word = word
    guess_word=('_' * len(word))
    trial = 0
    while trial < 6 and  guess_word != backup_word:
        print("Guess word", guess_word)
        guess_letter = input("Enter your guess ")
        check = word.find(guess_letter)

        if check == -1:
            trial += 1
            hangman_diagram(trial)
        else:
            while guess_letter in word:
                check = word.find(guess_letter)
                word = word[:check ] + '_' + word[ check+1:]
                guess_word = guess_word[:check] + guess_letter + guess_word[check+1:]
    if guess_word == backup_word:
        return True
    return False 
    

def hangman_diagram(trial):
    if trial == 1:
        print ('''
                     -------------
                    |            |
                   ( )           |
                                 |
                                 |
                                 |
                                 |
                                 | 
                                /| 
                             ========''') 
    if trial == 2:
        print ('''
                     -------------
                    |            |
                   ( )           |
                    |            |
                    |            |
                    |            |
                                 |
                                 | 
                                /| 
                             ========''') 
    if trial == 3:
        print ('''
                     -------------
                    |            |
                   ( )           |
                    |            |
                   /|            |
                  / |            |
                                 |
                                 | 
                                /| 
                             ========''') 
    if trial == 4:

        print ('''
                     -------------
                    |            |
                   ( )           |
                    |            |
                   /|\           |
                  / | \          |
                                 |
                                 | 
                                /| 
                             ========''') 

    if trial == 5:

        print ('''
                     -------------
                    |            |
                   ( )           |
                    |            |
                   /|\           |
                  / | \          |
                   /             |
                  /              | 
                                /| 
                             ========''') 

    if trial == 6:

        print ('''
                     -------------
                    |            |
                   ( )           |
                    |            |
                   /|\           |
                  / | \          |
                   / \           |
                  /   \          | 
                                /| 
                             ========''') 

while True:
    if main_game():
        print("You win")
        response = input('Do you want to continue [y/n] ').lower()
        if response == 'n':
            break
            

    else :
        print("You lose")

