#Day10-Calculator
from replit import clear;


class Calc:


    def pre_img():

         logo= '''                     
                    |  _________________  |
                    | | VM  3.141592654 | |
                    | |_________________| |
                    |  __ __ __ __ __ __  |
                    | |__|__|__|__|__|__| |
                    | |__|__|__|__|__|__| |
                    | |__|__|__|__|__|__| |
                    | |__|__|__|__|__|__| |
                    | |__|__|__|__|__|__| |
                    | |__|__|__|__|__|__| |
                    |  ___ ___ ___   ___  |
                    | | 7 | 8 | 9 | | + | |
                    | |___|___|___| |___| |
                    | | 4 | 5 | 6 | | - | |
                    | |___|___|___| |___| |
                    | | 1 | 2 | 3 | | x | |
                    | |___|___|___| |___| |
                    | | . | 0 | = | | / | |
                    | |___|___|___| |___| |
                    |_____________________|
                   
                   ''';
         print("\t\t\t\t\t\tCalculator\n=========================================================\t\t"+logo);

    def humpropmt():
        c.pre_img();

        option=int(input("Select the operation number you want to perform:\n1.Addition (+)\n2.Subtraction (-)\n3.Multiplication (x)\n4.Division (/)\n5.Root\n6.Trignometry\n-------------------\n:      ") );
        #while(option.is_integer()):

        if(option==1):
            flag=True;
            values=[];
            while(flag):
                values.append(input("Enter the number for addition (type 'exit' to quit): "));
                if(values[-1]=='exit'):
                    flag=False;
                    values.remove('exit')
                print(f"The sum of values {values} is: ", c.addt(values))


            print(f"The Final sum of values {values} is: ", c.addt(values))

        if(option ==2):
            a = int(input("Enter 1st number for subtraction: "));
            b = int(input("Enter 2nd number for subtraction: "));
            print(f"The value of {a}-{b} is: ", c.subt(a, b));

    def addt(a):

        sum=0;
        for i in range(0, len(a)):
           sum+=int(a[i]);
        return (sum);

    def subt(a, b):
        diff = 0;
        for i in range(0, len(a)):
            diff -= int(a[i]);
        return (diff);


    def mult(a, b):
        return (a*b);

    def divt(a, b):
        return (a/b);

c=Calc;
c.humpropmt();
#c.calbegin();
