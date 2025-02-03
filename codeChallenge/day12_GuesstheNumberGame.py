#Day12-Guess The Number
############### Guess the Number #####################
import random
from replit import clear;
gameType= {1:"easy", 2:"hard"};
gamechoice= {"easy": 10, "hard": 5}
_guessNumber=random.randint(1, 100);


class GuessNumber:

    def pre_img(self):
        img="""    
                 ___                      ___  _          _ _              _             
                /  _>  _ _  ___  ___ ___ |_ _|| |_  ___  | \ | _ _ ._ _ _ | |_  ___  _ _ 
                | <_/\| | |/ ._><_-<<_-<  | | | . |/ ._> |   || | || ' ' || . \/ ._>| '_>
                `____/`___|\___./__//__/  |_| |_|_|\___. |_\_|`___||_|_|_||___/\___.|_|  
                                                                                         
              """


        return img;


    def gameLogic(self, choiceValue):
        choice = gamechoice[gameType[choiceValue]];
        #userGuessNumber=;
        userGuessNumber = int(input(f"You have {choice} remaining to guess the NUmber: "));
        while userGuessNumber != _guessNumber and choice >0:
            choice -= 1;
            if (userGuessNumber == _guessNumber):
                print("You Guessed it correct. You WON!!!");
                break;
            elif (userGuessNumber >= _guessNumber + 10):
                userGuessNumber = int(input(f"You guess value is too high,  {choice} remaining to guess the Number: "));
            elif (userGuessNumber <= _guessNumber - 10):
                userGuessNumber = int(input(
                    f"You guess value is too low,  {choice} remaining to guess the Number: "));
            else:
                userGuessNumber = int(input(f"guessed value is too close, try again, {choice} remaining to guess the Number: "));
        if (userGuessNumber == _guessNumber):
            print("You Guessed it correct. You WON!!!");
        else:
            print("You ran out of choices. You LOOSE!!");

    def gameStarter(self):
        clear();
        print(self.pre_img());
        print("Welcome to NUmber Guessing Game...");
        print("Guess the Number i have thought.")

        print(_guessNumber);
        userGameTypeSelection= input("Select mode of Game(easy or hard): ").lower();
        if(userGameTypeSelection not in gameType.values()):
            print(f"Invalid game mode:{userGameTypeSelection}, restarting game");
            self.gameStarter();
        else:
            if(userGameTypeSelection == gameType[1]):
                 self.gameLogic(1)
            elif(userGameTypeSelection == gameType[2]):
                self.gameLogic(2)





# g= GuessNumber()
# g.gameStarter()