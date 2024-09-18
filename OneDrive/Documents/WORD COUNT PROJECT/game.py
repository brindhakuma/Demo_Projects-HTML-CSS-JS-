import random

words = ['programming','tiger','lamp','television','laptop','water',
'microscope','doctor','youtube',
'projects']

random_word = random.choice(words)


print('our random word', random_word)

print('*****WORD GUESSING GAME*****')
user_guess=''
chances=10
while chances > 0:
    wrong_guess = 0
    for char in random_word:
        if char in user_guess:
            print(f"correct guess:{char}")
        else:
            wrong_guess += 1
            print('-')
    if wrong_guess == 0:
            print("correct")
            print(f"word:{random_word}")
            break
    guess = input('make a guess:')
    user_guess += guess
    if guess not in random_word:
         chances -= 1
         print(f"wrong you have {chances} more chances")
         if chances == 0:
            print('game over')
            
         
