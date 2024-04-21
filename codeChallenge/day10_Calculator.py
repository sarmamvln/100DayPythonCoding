#Day10-Calculator
from replit import clear;
from math import sqrt, isqrt, sin, cos, tan;

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

    def calci():
        c.pre_img();
        flag = True;
        lastval=[];
        lastval.append(input("Enter the number: "));
        while (flag):
            clear();
            option = input(
                f"Select the operation corresponding number you want to perform:\n1.Addition (+)\n2.Subtraction (-)\n3.Multiplication (x)\n4.Division (/)\n5.Root\n6.Trignometry\n-------------------\n:      ");
            if(lastval[-1]=='exit'):
                flag=False;
                lastval.remove('exit')
            elif(option=='exit'):
                flag=False;
            else:
                if(option=='1'):
                    lastval.append(input("Enter the second number  (type 'exit' to quit): "));
                    lastval.append(c.addt(lastval))
                    print(f"The addition of  {lastval[-3]} and {lastval[-2]} is: ", lastval[-1]);

                if(option =='2'):
                    lastval.append(input("Enter the second number  (type 'exit' to quit): "));
                    lastval.append(c.subt(lastval));
                    print(f"The final value after subtraction of {lastval[-3]} and {lastval[-2]} is: ", lastval[-1]);

                if(option =='3'):
                    lastval.append(input("Enter the second number  (type 'exit' to quit): "));
                    lastval.append(c.mult(lastval))
                    print(f"The final value after multiplication of {lastval[-3]} and {lastval[-2]} is: ", lastval[-1])

                if(option =='4'):
                    lastval.append(input("Enter the second number  (type 'exit' to quit): "));
                    lastval.append(c.divt(lastval))
                    print(f"The final value after divison of {lastval[-3]} and {lastval[-2]} is: ", lastval[-1])

                if(option =='5'):
                    lastval.append(c.rut(lastval))
                    print(f"The root of values {lastval[-2]} is: ", lastval[-1]);

                if(option =='6'):
                    option = input(
                        f"Select the operation corresponding number you want to perform:\n1.Sin\n2.Cos\n3.Tan\n-------------------\n:      ");
                    if (option == '1'):
                        lastval.append(c.sinf(lastval))
                        print(f"The Sin of values {lastval[-2]} is: ", lastval[-1]);
                    if (option == '2'):
                        lastval.append(c.cosf(lastval))
                        print(f"The Cos of values {lastval[-2]} is: ", lastval[-1]);
                    if (option == '3'):
                        lastval.append(c.tanf(lastval))
                        print(f"The Tan of values {lastval[-2]} is: ", lastval[-1]);

    def addt(a):
        if(len(a)<=2):
            return float(a[0])+float(a[1]);
        else:
           return float(a[-1])+float(a[-2]);

    def subt(a):
        if(len(a)<=2):
            return float(a[0])-float(a[1]);
        else:
           return float(a[-2])-float(a[-1]);

    def mult(a):
        if(float(a[-1])==0):
            return 0;
        elif(len(a)<=2):
            return float(a[0])*float(a[1]);
        else:
           return float(a[-2])*float(a[-1]);
    def divt(a):
        if(float(a[-1])==0):
            return 0;
        elif(len(a)<=2):
            return float(a[0])/float(a[1]);
        else:
           return float(a[-2])/float(a[-1]);
    def rut(rootnum):
        if(rootnum[-1]!='exit'):
            return sqrt(float(rootnum[-1]));
        elif(rootnum[-1]<0):
            return 'i';
        else:
            return False;
    def sinf(a):
        return sin(float(a[-1]));
    def cosf(a):
        return cos(float(a[-1]));
    def tanf(a):
        return tan(float(a[-1]));


c=Calc;
c.calci();

