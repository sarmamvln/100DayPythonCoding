# Day 02 Tip Calculator.

class tipCalculator:
    print("Welcome to the tip calculator.");

    def tip_cal(total_bill, number_of_people):

        tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "));
        while (tip_percent not in [10,12,15]):
            print("Enter any value of 10, 12 or 15.");
            tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "));


        final_amount = total_bill + (total_bill * int(tip_percent) / 100);
        print("Each person should pay: $", round(final_amount / number_of_people,2));

    def totalbill():
        total_bill = input("What was total bill? $");
        total_bill_amount = int(total_bill.strip('$'));

        number_of_people = input("How many people to split the bill? ");
        # Number of people validation
        while (number_of_people.isnumeric() is not True):
            print("Enter valid input, input should be numeric and not null.")
            number_of_people = input("How many people to split the bill? ")

        tipCalculator.tip_cal(total_bill_amount, int(number_of_people));


    #totalbill();

t1=tipCalculator;
t1.totalbill();
