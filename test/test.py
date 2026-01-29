import os
import random
from creators.configs.required_data import CATEGORIES

string = "qwertyuiopasdfghjklzxcvbnm"

letters = []
for letter in string:
    letters.append(letter)

for i in range(10):
    for category, extension in CATEGORIES.items():
        if extension[0] != "":
            name_file = random.choice(letters) + random.choice(extension)
            path = os.path.join("/home/user/Trash", name_file)
            with open(path, "w"):
                pass
