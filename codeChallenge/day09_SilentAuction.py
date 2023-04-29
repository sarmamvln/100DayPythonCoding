#Day09-SilentAuction
import pprint
from replit import clear

class silentAuction:

    def logo():

        logo= '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                        `'-------'`    
        
        '''

        print(logo);

        print("\n", "Welcome to the Secret Auction program\n(Shhhhh....Silence Auction in progress)")

    def aution():
        silentAuction.logo()
        auction_tracker={}

        auction_name=input("Enter your name to participate in Auction: \n");
        auction_bid=input("Enter you bid amount: \n$")

        auction_tracker[auction_name]=auction_bid.strip("$");
        flag=input("Are there any other bidders(yes/no): \n").lower();
        if flag=='yes':
            clear();
            silentAuction.aution();
        else:
            print("Results will be declared shortly....")
            max=0;
            winkey="";

            for key in auction_tracker:
                if int(auction_tracker[key])>max:
                    winkey=key

            auction_tracker.get(winkey)
            print(f"The winner is {winkey.title()} and the bid amount is ${auction_tracker[winkey]} ")







#sa=silentAuction;
#sa.aution();