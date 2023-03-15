#Day 01 Band name suggetion.
class bandName:

    def suggetion():

        print("Welcome to the Band Name Generator.");
        city = input("What's name of city you grew up in?");
        while (city.isalpha()==False):
            print("Input accepts alphabetics only, Please retry");
            city = input("What's name of city you grew up in?").title();
            if (city.isalpha() == False):
                continue;
            elif (city.isalpha() == True):
                break;

        pet = input("What's your pet's name");
        while (pet.isalpha() == False):
            print("Input accepts alphabetics only, Please retry");
            pet = input("What's your pet's name").title();
            if (pet.isalpha() == True):
                break;
            elif (pet.isalpha() == False):
                continue;

        print("Your band name could be ", city.title() + " " + pet.title())
        # return city.join(" ")+pet;

    suggetion();
