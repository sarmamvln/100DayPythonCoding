from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray


class User:
    def __init__(self, id, name):
        self.id= id
        self.username= name
        self.followers= 0
        self.following= 0

    def follow(self, user):
        user.following+=1
        self.followers+=1



user_1= User("001", "Test1")

print(user_1.username)

user_2= User("002", "Test2")
user_3= User("003", "Test3")

user_1.follow(user_2)
user_3.follow(user_1)
user_2.follow(user_1)

print(user_1.following)
print(user_1.followers)
print()
print(user_2.following)
print(user_2.followers)
print()
print(user_3.following)
print(user_3.followers)