#Day11-BlackJackCapstoneProject
#Game Requirements - cannot go sum more than 21 , i fmor ethan 21 calledas Bust, the person who gets more number by combining cards is winner
# values 2-10 cards are same , J,Q,K - are each counted as 10, A -can be 1 or 11, if <17 must take another card
############### Blackjack Project #####################
import random

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from replit import clear;



class BlackJack:

    def pre_img():
        img=''' 
                88          88                       88        88                       88         
                88          88                       88        ""                       88         
                88          88                       88                                 88         
                88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
                88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
                88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
                88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
                8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                              ,88                                  
                                                          888P"                                  
              '''


        return img;


    def draw_A_Card():
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'K', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'K', 'J', 'A', 2, 3, 4,
                5, 6, 7, 8, 9, 10, 'Q', 'K', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'K', 'J', 'A'];
        deckval = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Q': 10, 'K': 10, 'J': 10, 'A': 11}
        randomgenerator =int( random.randint(0, len(deck) - 1));
        random.shuffle(deck);
        return int(deckval[deck[randomgenerator]]);

    def winloose_default(bet="defaultwin", amount=50):
        winmultiplyer = {"defaultwin": 2, "Blackjack": 1.5,  "push": 1, "surrender": 0.5,
                         "insurance": 0.5}

        return float(winmultiplyer[bet]*amount);

    def winloose_custom(bet=3, amount=50):
            if(bet>10):
                return print("bet cannot be more than 10x");
            elif(bet in range(3, 11)):
                return float(bet*amount);


    def betAmt(money=1000):
        chips = {"white": 1, "red": 5, "green": 25, "blue": 50, "black": 100, "purple": 500}
        betamount=input(f"You currently have {money}, how much you want to bet: ");
        if(int(betamount)>money or int(betamount)<0):
            bet = input(f"Sorry, You cannot bet more than available {money} or lestt than 0 amount, retry\n how much you want to bet: ");

        return float(betamount);


    def finalMoney(status=1, betamt=0, amt=1000, wintype='defaultwin'):
        if(status==1):
            return float(amt+b.winloose_default(amount=betamt, bet=wintype));
        elif(status==0):
            return float(amt-b.winloose_default(amount=betamt, bet=wintype));




    def blackjackproj():
        print(b.pre_img());
        currplayerAmt=1000;
        currdealerAmt=1000;

        customwinbet = 3;

        flag=True;

        while(flag):
            clear()
            player = [];
            dealer = [];
            print(f"Dealer Amount: {currdealerAmt} \t\tPlayer Amount: {currplayerAmt}\n")
            betamt = b.betAmt(money=currplayerAmt);
            i = 1
            for i in range(1, 3):
                player.append(b.draw_A_Card());
                dealer.append(b.draw_A_Card());
                i += 1;
            while (sum(player) < 16):
                player.append(b.draw_A_Card());
            while (sum(dealer) < 16):
                dealer.append(b.draw_A_Card());


            if(sum(player)>21):
                if('11' in player):
                    player.remove(11)
                    player.append(1)
                currdealerAmt = b.finalMoney(betamt=betamt, amt=currdealerAmt)
                currplayerAmt = b.finalMoney(0, betamt=betamt, amt=currplayerAmt)
                print(f"Player BUST!! Dealer is winner, Congratulations, \n Dealer Amount is  ${currdealerAmt} \nPlayer Amount is  ${currplayerAmt} ");

            elif(sum(dealer)>21):
                currplayerAmt = b.finalMoney(betamt=betamt, amt=currplayerAmt)
                currdealerAmt = b.finalMoney(0, betamt=betamt, amt=currdealerAmt)
                print(f"Dealer BUST!! Player  is winner, Congratulations, \n Player Amount is  ${currplayerAmt} \n Dealer Amount is  ${currdealerAmt}");

            elif(sum(player)<21 and sum(player)>sum(dealer)):
                currplayerAmt = b.finalMoney(betamt=betamt, amt=currplayerAmt)
                currdealerAmt = b.finalMoney(0, betamt=betamt, amt=currdealerAmt)
                print(f"WIN!! Player won, Congratulations!!! \n Player Amount is  ${currplayerAmt} \n Dealer Amount is  ${currdealerAmt}");

            elif(sum(dealer)<21 and sum(dealer) > sum(player)):
                currdealerAmt = b.finalMoney(betamt=betamt, amt=currdealerAmt)
                currplayerAmt = b.finalMoney(0, betamt=betamt, amt=currplayerAmt)
                print(f"WIN!! Dealer won, Congratulations!!!\n Dealer Amount is  ${currdealerAmt} \nPlayer Amount is  ${currplayerAmt} ");

            elif (sum(player) ==21):
                currplayerAmt = b.finalMoney(betamt=betamt, amt=currplayerAmt, wintype='Blackjack')
                currdealerAmt = b.finalMoney(0, betamt=betamt, amt=currdealerAmt, wintype='Blackjack')
                print(f"Blackjack, Player is winner. Congratulations!!! \n Player Amount is  ${currplayerAmt} \n Dealer Amount is  ${currdealerAmt}");

            elif (sum(dealer)== 21):
                currdealerAmt = b.finalMoney(betamt=betamt, amt=currdealerAmt, wintype='Blackjack')
                currplayerAmt = b.finalMoney(0, betamt=betamt, amt=currplayerAmt, wintype='Blackjack')
                print(f"Blackjack, Dealer is winner. Congratulations!!! \n Dealer Amount is  ${currdealerAmt} \nPlayer Amount is  ${currplayerAmt} ");


            print("player value",player);
            print("player sum=", sum(player))
            print("dealer 1st value", dealer[0]);
            #print("dealer sum=",sum(dealer))

            if(currplayerAmt>0):
                op=input("do you want to conitnue 'y' or 'n' : ")
                if(op.lower()!='y' or currplayerAmt==0):
                    flag=False;
                    print(f"Final Amounts are: \nDealer-{currdealerAmt} \tPlayer-{currplayerAmt}");
            else:
                flag = False;
                print(f"Final Amounts are: \nDealer:{currdealerAmt} \tPlayer:{currplayerAmt}");






ch=input("Do you want to play a game of Blackjack 'y' or 'n' : ")
if(ch.lower()=='y'):
    b = BlackJack;
    b.blackjackproj();

else:
    foo = False;
    print("Bye!!!")

