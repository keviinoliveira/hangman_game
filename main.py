import random
import hangman_art as ha
import hangman_words as hw

random_word = random.choice(hw.word_list)
number_letters = len(random_word)
placeholder = []
for a in range(0, number_letters):
    placeholder.insert(a,'_')

print(ha.hangman)

check_letters= ""
life = 6
while life > 0:
    print(f"Word to guess: {''.join(placeholder)}")
    letter = input ("Guess a letter: ").lower()
    check = 0
    print(f"You've already guessed {letter}")
    if letter in check_letters:
        print("Choose outher letter")
        print(ha.steps[-life-1])
        print(f"****************************{life}/6 LIVES LEFT****************************")
        continue
    else:
        check_letters += letter
    for index, ltr in enumerate(random_word):
        if (ltr == letter):
            placeholder[index] = letter
            check = 1
    print(''.join(placeholder))
    if '_' not in ''.join(placeholder):
        print("**************************** Congratulations! :) ****************************")
        break
    elif check == 0:
        life -= 1
    print(ha.steps[-life-1])
    print(f"****************************{life}/6 LIVES LEFT****************************")
if life == 0:
    print(f"**************************** You lose! :( It was {random_word} ****************************")

