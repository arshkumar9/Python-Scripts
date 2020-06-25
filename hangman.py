import random
def random_word():
    f = open('american-english', 'r')
    content = f.read().splitlines()
    f.close()
    return random.choice(content)

def main_game():
    word = random_word().lower()
    print(word)
    guess_word=('_' * len(word))
    trial = 0
    while trial < 6 and  guess_word != word:
        print("Guess word", guess_word)
        guess_letter = input("Enter your guess ")
        check = word.find(guess_letter)

        if check == -1:
            trial += 1
            hangman_diagram(trial)
            print(trial)
        else:
            print(check)
            guess_word = guess_word[:check] + guess_letter + guess_word[check+1:]
    return None
    

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
string = "Hello"
if 's' in string:
    print("s")
elif 'H' in string:
    print("helo")
print(len(string))
main_game()
