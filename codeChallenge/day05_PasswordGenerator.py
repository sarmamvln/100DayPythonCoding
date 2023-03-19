#Day 05 - Password Generator
import random


class passwordGenerator:

    def data_feed():
        '''
        #full_map= {}
        #for ascii_code in range(0, 512):
        #    full_map[ascii_code]=chr(ascii_code)
        #print(full_map)
        '''
        caps_alpha_list=[]
        lower_alpha_list = []
        special_printable_list = []   #'@', '#', '$', '^', '*', '!'
        digit_list=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

        for ascii_code in range(65, 91):
            caps_alpha_list.append(chr(ascii_code));
        for ascii_code in range(97, 123):
            lower_alpha_list.append(chr(ascii_code));
       #limited asciii to only 256
        for ascii_code in range(1, 257):
            if chr(ascii_code) not in caps_alpha_list and chr(ascii_code) not in lower_alpha_list and  chr(ascii_code)  not in  digit_list:
                 if chr(ascii_code).isprintable()==True:
                     special_printable_list.append(chr(ascii_code));

        pwd_list_chars= [caps_alpha_list, lower_alpha_list, digit_list, special_printable_list]
        #print(caps_alpha_list)
        #print("===================")
        #print(lower_alpha_list)
        #print("===================")
        #print(len(special_printable_list))
        #print("===================")
        #print(special_printable_list)
        #print("===================")
        return pwd_list_chars;

    def pwdGenerator():
        upperchar=passwordGenerator.data_feed()[0]
        lowerchar=passwordGenerator.data_feed()[1]
        digits=passwordGenerator.data_feed()[2]
        special=passwordGenerator.data_feed()[3]
        len_of_pwd= int(input("How many characters would you like to be in your password? "))
        while (len_of_pwd not in range(8, 25)):
            print("Your input is NOT valid, Retry."+"\n HINT: Password length should be minimum 8 maximum 25, and number value only accepted")
            len_of_pwd = int(input(" How many characters would you like to be in your password? ").strip(" "))


        special_symbols_in_pwd= int(input("How many special characters would you like to have in your password? "))
        while (special_symbols_in_pwd==0 or special_symbols_in_pwd>=len_of_pwd):
            print("Your input is NOT valid, Retry."+"\n HINT: Special chars should not be Null or equal to  length of password")
            special_symbols_in_pwd = int(input("How many special characters would you like to have in your password? ").strip(" "))

        numbers_in_pwd = int(input("How many numbers would you like to have in your password? "))
        while (numbers_in_pwd==0 or numbers_in_pwd>=len_of_pwd or ((special_symbols_in_pwd+numbers_in_pwd)>len_of_pwd-2)):
            print("Your input is NOT valid, Retry."+"\n HINT: Password should have atleast one Numbers and password should not only contain numbers or special chars i.e numbers + special chars should not exceed max length of password")
            numbers_in_pwd = int(input("How many numbers would you like to have in your password? ").strip(" "))

        recommended_pwd="";
        number_of_aplhabets=len_of_pwd - (numbers_in_pwd+special_symbols_in_pwd);
        recommended_pwd_alpha= []
        recommended_pwd_special =[]
        recommended_pwd_number = []
        while len(recommended_pwd_alpha)<number_of_aplhabets-1:
            recommended_pwd_alpha.append(random.choice(upperchar))
            recommended_pwd_alpha.append(random.choice(lowerchar))


        while len(recommended_pwd_number) <= numbers_in_pwd-1:
            recommended_pwd_number.append(random.choice(digits))



        while len(recommended_pwd_special)<=special_symbols_in_pwd-1:
            recommended_pwd_special.append(random.choice(special))

        recommended_pwd = "".join(recommended_pwd_alpha).join(recommended_pwd_special).join(recommended_pwd_number)

        print(f"*Your Recommended password is : {recommended_pwd}")


#p1=passwordGenerator
#p1.pwdGenerator()