#Day15-Coffee Machine
# """
# ####REQUIREMENTS####
# Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
# """
############### Coffee Machine #####################
import random
from replit import clear;
from PIL import Image;



class CoffeeMachine:
    refill_flag= False;
    MENU= {
        "espresso" : {
            "ingredients" : {
                "water" : 50,
                "coffee" :  18,
            },
            "cost" : 1.5
        }
        ,
        "latte" : {
            "ingredients" : {
                "water" : 200,
                "milk" : 150,
                "coffee" :  24,
            },
            "cost" : 2.5
        }
        ,
        "capaccino" : {
            "ingredients" : {
                "water" : 250,
                "milk" : 100,
                "coffee" :  24,
            },
            "cost" : 3.0
        }
        ,
    }


    machineMaxCapacity= {"water": 1000, "milk": 1000, "coffee": 500}
    currentIngrendiends = machineMaxCapacity
    machineIngredientsCapacityUnits = {"water": "ml", "milk": "ml", "coffee": "gms"}
    priceDenomination= {"penny":0.01,"nickel":0.05, "dime": 0.10, "quarter": 0.25, "dollar": 1}
    machineStatus= "on"
    quantitysaled= {"espresso": 0, "latte":0, "capaccino":0}
    saledprice = {"espresso": 0, "latte":0, "capaccino": 0}
    userCurrency= {"penny":0,"nickel":0, "dime": 0, "quarter": 0, "dollar": 0}

    def game_img(self):
         #img= Image.open("./imgs/day15_CoffeeMachine/coffeemachine_.jpg");
         img2= """
                            /~~~~~~~~~~~~~~~~~~~/|
                           /              /######/ / |
                          /              /______/ /  |
                         ========================= /||
                         |_______________________|/ ||
                          |  \****/     \__,,__/    ||
                          |===\**/       __,,__     ||    
                          |______________\====/%____||
                          |   ___        /~~~~\ %  / |
                         _|  |===|===   /      \%_/  |
                        | |  |###|     |########| | /
                        |____\###/______\######/__|/
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~              
         
            """
         return img2;

    def totalMoneyafterSales(self):
        for each in self.saledprice.keys():
            self.saledprice[each] += self.MENU[each]["cost"]*self.quantitysaled[each]
            print(f" {each}:  $ {self.saledprice[each]}")

    def priceHandler(self, drinkCost):
        currentuserprice=0
        print(f"The cost of selected drink is ${drinkCost} ");
        print(f"Accepted denomination are {self.priceDenomination.keys()}")
        for key in self.priceDenomination.keys():
            self.userCurrency[key]= int(input(f"Enter number of {key.upper()} coins : "))
            currentuserprice+= self.priceDenomination[key]*self.userCurrency[key]
        if(currentuserprice>=drinkCost) :
            print(f"You entered total amount is ${currentuserprice} and required drink price is ${drinkCost}, You get refund of ${currentuserprice-drinkCost}.Enjoy your coffeee")

        else:
            print(f"You entered amount is ${currentuserprice} and required drink price is ${drinkCost},  less by ${drinkCost-currentuserprice}")
            self.priceHandler(drinkCost)

    def refillIngredients(self):
        self.machineStatus= "off"
        print("Total collected money summary by each product:  ")
        self.totalMoneyafterSales()


        if(self.refill_flag):
            self.currentIngrendiends=self.machineMaxCapacity;
            print("Ingredients refilled successlly");
            self.refill_flag=False



    def ingredientsChecker(self, menuId):

        for key in self.MENU[menuId]["ingredients"]:
            if(self.currentIngrendiends[key] < self.MENU[menuId]["ingredients"][key]):
                print("Minimum required ingredients NOT available, you may want refill");
                try:
                    refillFlag = input("Do you want to refill now('off' or 'skip' ): ");
                except ValueError:
                    print("Please Enter 'off' to power off machine and refill or skip  \n ");
                    refillFlag = input("Do you want to refill now('off' or 'skip' ): ");
                if (refillFlag.lower() == 'off'):
                    self.refill_flag = True
                    print("Switching off machine for Refill.. Please wait.")
                    self.refillIngredients();
                else:
                    print("Sorry not able to brew required drink as Ingredients are Low.Wait for refill of ingredients...");
                    self.refill_flag= True;
                    break;
            else:
                continue

        if(self.refill_flag!= True):

            for each in self.MENU[menuId]["ingredients"].keys():
                self.currentIngrendiends[each]-=self.MENU[menuId]["ingredients"][each]

            self.quantitysaled[menuId] += 1;
            print(f"The price for the selected drink is ${self.MENU[menuId]["cost"]}")

            try:
                priceEntryFlag = input("Are you ready to enter coins('Y' or 'N'): ");
            except ValueError:
                print("Please Enter 'Y' for 'Yes' or 'N' for 'No', try again \n ");
                priceEntryFlag = input("Are you ready to enter coins('Y' or 'N'): ");
            if (priceEntryFlag.lower() == 'y'):
                self.priceHandler(self.MENU[menuId]["cost"])
            else:
                print("NO free drinks...");



    def drinkSelectionHandler(self, menuId):
        self.ingredientsChecker(menuId);


    def coffeeMachine(self):

        clear()
        print(self.game_img())
        while(self.machineStatus== 'on'):
            drinkSelection= input("\n1.Espresso\n2.Latte\n3.Capaccino\nWhat would you like? ")
            # while(drinkSelection.lower() not in self.availableDrinks.values() or drinkSelection not in self.availableDrinks.keys()):
            #     print("Select only from available options, Enter either corresponding number or drink name")
            #     drinkSelection = input("\n1.Espresso\n2.Latte\n3.Capaccino\nWhat would you like? ")
            #
            # self.drinkSelectionHandler(self.MENU[drinkSelection.lower()])

            if(drinkSelection.lower()=="espresso" or drinkSelection=='1'):
                self.drinkSelectionHandler("espresso")
            elif(drinkSelection.lower()=="latte" or drinkSelection=='2'):
                self.drinkSelectionHandler("latte")
            elif(drinkSelection.lower()=="capaccino" or drinkSelection=='3'):
                self.drinkSelectionHandler("capaccino")
            elif(drinkSelection.lower()=="report"):
                print("\nBelow is current Ingredients status of the Machine ")
                for each in self.currentIngrendiends.keys():
                    print(f" {each}:  {self.currentIngrendiends[each]} {self.machineIngredientsCapacityUnits[each]}")
            else:
                self.machineStatus= "pause"




cm= CoffeeMachine();
cm.coffeeMachine();
