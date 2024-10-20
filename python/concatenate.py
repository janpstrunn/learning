import os

user_home = "/home/$USER/"

user_folder = input("What folder do you have at" + user_home + "?\n")

full_path = os.path.join(user_home, user_folder + "/")

print("The concatenated path is:", full_path)

