import argparse
import os
import sys

import yaml

data_yaml = "data.yaml"


def main():

    args = parser.parse_args()

    if args.create:
        create_user()
    elif args.show:
        show()
    elif args.login:
        login()
    elif args.delete:
        delete()


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

    parser = argparse.ArgumentParser(description="Command-line tool github config global")
    parser.add_argument('-c', '--create', action="store_true", help="Create something")
    parser.add_argument('-s', '--show', action="store_true", help="Show my login")
    parser.add_argument('-l', '--login', action="store_true", help="Login to an account")
    parser.add_argument('-d', '--delete', action="store_true", help="Delete something")
    parser.add_argument('-e', '--edit', action="store_true", help="Edit something")

    #lunch()
    main()

    print("Lunch with no error.")
