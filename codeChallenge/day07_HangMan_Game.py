#Day 07 - HangMan Game
import random


from PyDictionary import PyDictionary as dict
from bs4 import BeautifulSoup as soup

class HangManGame:
    def intro_art():
        print('''        
             _                                             
            | |                                            
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ \/ _` | '_ \ \/ _` | '_ ` _ \ \/ _` | '_ \ 
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __\/ |                      
                               |___\/           
            ''' );

    def word_generator():
        word_list=["beautiful", "onion orange", "coders Logins", "not"]
        random.shuffle(word_list)
        game_guess_word=random.choice(word_list)
        return game_guess_word

    def hangman(flag_counter,flag=True):

        hangman_art=[
            '''    
          +---+
          |   |
          O   |
              |
              |
              |
        =========        
        ''', '''
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
        ========='''
        ]
        if (flag_counter!=len(hangman_art)):
            print(hangman_art[flag_counter-1]);
            flag = True
        else:
            print(hangman_art[-1]);
            print("Game_Over")
            flag=False;
        return flag;


    def user_input_validator(user_guess):
        flag=True
        while flag:
            if ascii(user_guess) in range(97, 124):
               flag= False
            else:
                print("not valid input, Try again!!!")




    def user_game_start(game_word=word_generator().lower(),flag=True):
        HangManGame.intro_art()
        display=[]
        for letter in range(len(game_word)):
            display.append("_ ")
        guess_word="".join(display)
        print(guess_word)
        user_guess= input("Guess a letter: ");
        wrong_guess_counter=0;
        while flag:
            if user_guess not in game_word:
                wrong_guess_counter += 1
                print(f"You guessed letter {user_guess}, that's NOT in the word.You lose a life!!!")
                print('-------------------')
                flag= HangManGame.hangman(wrong_guess_counter, flag);

            else:
                for x in range(len(game_word)):
                    if user_guess==game_word[x]:
                         display[x]=user_guess
                guess_word = "".join(display)
            print(guess_word)
            if guess_word==game_word:
                print("Congratulations!!! You guessed the word correctly.")
                flag=False
            else:
                user_guess =input("Guess a letter: ");








hm=HangManGame;
hm.user_game_start()

