#Day 08 - Ceagar Cipher

class ceagerCipher:

    def intro_banner():
        logo = """           
         ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
        a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
        8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
        "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
         `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                    88             88                                 
                   ""             88                                 
                                  88                                 
         ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
        a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
        8b         88 88       d8 88       88 8PP""""""" 88          
        "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
         `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                      88                                             
                      88           
        """
        print(logo)

    def cipher_data_feed():
        datafeed=[]
        #for ascii_code in range(65, 91):
        #    datafeed.append(chr(ascii_code));
        #for x in range(0, 10):
        #    datafeed.append(x);
        for ascii_code in range(97, 123):
            datafeed.append(chr(ascii_code))

        return datafeed

    def userMessage():
        ceagerCipher.intro_banner()
        #msg_mapper={}
        #code_name= input("Enter the code name  to capture your secret message: \n")
        flag = False
        while not flag:
            msg_task = input("Type 'encode' to encrypt your message, Type 'decode' to decrypt your message.")
            usr_msg = input("Type your message: \n" ).lower()
            salt = int(input("Enter your shift number: \n"))
            if salt>26:
                salt=salt%26


            ceagerCipher.cipher_message(usr_msg, salt, msg_task)

            bool_check= input("Do you wnat to continue?(Y/N): \n").lower()
            if bool_check=='n':
                flag=True
                print("Goodbye")



    def cipher_message(usr_msg, shift, msg_task):
        raw_data= ceagerCipher.cipher_data_feed()
        desired_text = ""

        if msg_task=="decode":
            shift*=-1
        for char in usr_msg:
            if char in raw_data:
                current_pos = raw_data.index(char)
                new_position = current_pos + shift
                if new_position > len(raw_data) - 1:
                    new_position = (current_pos - len(raw_data)) + shift
                encode_char = raw_data[new_position]
                desired_text += encode_char
            else:
                desired_text += char

        print(f"The {msg_task}d text is: {desired_text}")






#c1= ceagerCipher
#c1.userMessage()