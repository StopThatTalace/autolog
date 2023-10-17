import os
import sys

import yaml

data_yaml = "data.yaml"


def create_user():

    new_user = {
        input("Enter a name for this new login (work, school, home etc..):"): {
            "name": input("Enter the NAME of your github account:"),
            "email": input("Enter the EMAIL of your github account:")
        }
    }

    with open(data_yaml, 'w') as data:
        yaml.dump(new_user, data, default_style='\'"')


# os.system("git config --global user.name ")  # user etc
if __name__ == "__main__":
    print("Lunch with no error.")
