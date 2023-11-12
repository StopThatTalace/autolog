import argparse
import yaml
import os

class Autolog:
    def __init__(self, data_yaml="data.yaml"):
        self.data_yaml = os.path.join(os.path.dirname(os.path.abspath(__file__)), data_yaml)
        self.users = {}

    def main(self):
        args = self.parser.parse_args()

        if args.create:
            self.create_user()
        elif args.show:
            self.show()
        elif args.login:
            self.login()
        elif args.delete:
            self.delete()
        elif args.edit:
            self.edit()

    def create_user(self):
        user_category = input("Enter a name for this new login (work, school, home etc..):")
        self.users[user_category] = {
            "name": input("Enter the NAME of your github account:"),
            "email": input("Enter the EMAIL of your github account:")
        }

        with open(self.data_yaml, 'w') as data:
            yaml.dump(self.users, data, default_style='\'"')

    def show(self):
        print("[+] Showing logins")
        if not self.users:
            print("[-] No logins available.")
        else:
            for category, user_info in self.users.items():
                print(f"{category}: Name - {user_info['name']}, Email - {user_info['email']}")

    def setup_parser(self):
        self.parser = argparse.ArgumentParser(description="Command-line tool for GitHub config global")
        self.parser.add_argument('-c', '--create', action="store_true", help="Create something")
        self.parser.add_argument('-s', '--show', action="store_true", help="Show my login")
        self.parser.add_argument('-l', '--login', action="store_true", help="Login to an account")
        self.parser.add_argument('-d', '--delete', action="store_true", help="Delete something")
        self.parser.add_argument('-e', '--edit', action="store_true", help="Edit something")

if __name__ == "__main__":
    autolog = Autolog()
    autolog.setup_parser()
    autolog.main()
