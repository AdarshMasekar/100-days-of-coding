import random 
words = ['abhijeeet','abhilasha','adarsh','aishwarya','anusha','harish','karthik','shreeshail','anvita','chaitali','shejal']
# print(words)

word = words[random.randint(0,len(words)-1)]
word = list(word)
print(len(word)) 
"""
if you want to know the random word selected print

print(word)
"""
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
count = 0
guess = ""
while(len(word) != 0 ):
    # for i in range(0,len(words)-1):
    letter = input('enter a letter:')
    if(letter in word):
        print('your guess is correct keep going')
        word.remove(letter)
        # print(word)
    else:
        print('you guessed a wrong letter ')
        count += 1 
        if count < len(HANGMANPICS):
            print(HANGMANPICS[count])
        else:
            print('Sorry, You lost the game try again!')
            break

if count < len(HANGMANPICS):
    print('you won the game congratulations!')
    print("""
      O   
     \|/
      |
     / \ """)
