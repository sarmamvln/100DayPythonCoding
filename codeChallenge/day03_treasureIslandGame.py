# Day 03 Treasure Island Game.
import random
import time


class TreasureIsland:

    def preImage():
        #
        print('''
        *******************************************************************************
                  |                   |                  |                     |
         _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                  |                `"=._o`"=._      _`"=._                     |
         _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
         _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        ''')

    def preGametext():
        initalStr = 'Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou\'re at a cross road.Where do you want to go? Type "left" or "right"'
        print(initalStr)

    def gameFlow():
        TreasureIsland.preImage();
        TreasureIsland.preGametext();

        decision = input();
        if decision.lower() == "left":
            decision = input('Ah!!! you reached to a beach, what do you want to do("Swim" or "Wait"): \n');
            if decision.lower() == "wait":
                print("Wise Decision!!!")
                time_wait=time.sleep(5);
                while time_wait==0 or decision.lower() == "wait":
                    decision = input('What do you want to do "Explore" or "Wait":\n');
                    if decision.lower() == "wait":
                        time_wait=time.sleep(5);
                    if decision.lower() == "explore":
                        while decision.lower() == "explore":
                            k = random.choices(["RED", "BLUE", "YELLOW"]);
                            decision = input(f'you found a {k} door, what do you want to do "Enter" or "Explore" ');
                            if decision.lower()=="enter" and k[0]=="YELLOW":
                                print("You WON!!! Found the treasure");
                            elif decision.lower()=="enter" and k[0]=="BLUE":
                                print("oh NO!!! LARGE BEASTS \n you were nice soup for them.");
                            elif decision.lower()=="enter" and k[0]== "RED":
                                print("FIRE!!!FIRE!!!FIRE!!! \n you were burned.");
            else:
                print("Noooooo, A trout, you were attached by it.")
                print("GAME OVER!!!")
        else:
            print("You were NOT concisious, you fell into a giant HOLE.")
            print("GAME OVER!!!")









t1=TreasureIsland;
t1.gameFlow();
