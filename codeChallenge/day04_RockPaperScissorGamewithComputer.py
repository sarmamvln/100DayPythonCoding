# Day 04 Rock Paper Scissor Game.
import random


class RockPaperScissorGame:

    def visuals(request):

        img={"Rock": '''
                _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)      
           
                 ''',
         "Paper": '''   _______
                 ---'   ____)____
                            ______)
                          _______)
                         _______)
                ---.__________)
        
                ''',
         "Scissors": '''
                        _______
                    ---'   ____)____
                              ______)
                           __________)
                          (____)
                    ---.__(___)
              
                    '''}

        print(img.get(request));


    def game():
        game_mapping={0:"Rock", 1:"Paper", 2:"Scissors"};
        user_choice=int(input(f"What do you want to choose, {game_mapping} "));
        print("You choose " + game_mapping.get(user_choice));
        RockPaperScissorGame.visuals(game_mapping.get(user_choice));
        computer_choice=random.randint(0,2);
        print("Computer choose " + game_mapping.get(computer_choice));
        RockPaperScissorGame.visuals(game_mapping.get(computer_choice));
        RockPaperScissorGame.game_decision(user_choice, computer_choice)

    def game_decision(user_choice, computer_choice):
        '''
        Rock wins against scissors.

        Scissors win against paper.

        Paper wins against rock.

        '''
        if(computer_choice=="Rock" and user_choice=="Paper"):
            print("You won!!!")
        elif(computer_choice=="Rock" and user_choice=="Scissors"):
            print("You Lost!!! Better Luck Next Time.")
        elif (computer_choice == "Paper" and user_choice == "Scissors"):
            print("You Lost!!! Better Luck Next Time.")
        elif (computer_choice == "Paper" and user_choice == "Rock"):
            print("You won!!!")
        elif (computer_choice == "Scissors" and user_choice == "Rock"):
            print("You won!!!")
        else:
            print("You Lost!!! Better Luck Next Time.")





#r1= RockPaperScissorGame;
#r1.game()