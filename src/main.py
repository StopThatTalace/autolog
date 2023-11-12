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
        user_category = input("[+] Enter a name for this new login (work, school, home etc..):")

        if os.path.exists(self.data_yaml):
            with open(self.data_yaml, 'r') as data_file:
                self.users = yaml.safe_load(data_file)


        self.users[user_category] = {
            "name": input("[+] Enter the NAME of your github account:"),
            "email": input("[+] Enter the EMAIL of your github account:")
        }

        with open(self.data_yaml, 'w') as data:
            yaml.dump(self.users, data, default_style='\'"')

    def show(self):
        print("[+] Showing logins")
        if not os.path.exists(self.data_yaml):
            print("[-] No file available.")
        else:
            with open(self.data_yaml, 'r') as data_file:
                self.users = yaml.safe_load(data_file)

            if not self.users:
                print("[-] No logins available.")
            else:
                for category, user_info in self.users.items():
                    print(f"{category}: {user_info['name']} - {user_info['email']}")

    def login(self):
        category = input("[+] Enter the name of the login category you want to use: ")
        if not os.path.exists(self.data_yaml):
            print("[-] No file or no USER found.")

        else:
            with open(self.data_yaml, 'r') as data_file:
                self.users = yaml.safe_load(data_file)

            if category in self.users:
                print(f"[+] Logging in as {self.users[category]['name']}")
                os.system(f"git config --global user.name {self.users[category]['name']}")
                os.system(f"git config --global user.email {self.users[category]['email']}")
            else:
                print(f"[-] Login category '{category}' not found.")

    def delete(self):
        category = input("[+] Enter the name of the login category you want to DELETE: ")

        if not os.path.exists(self.data_yaml):
            print("[-] No file or no USER found.")
            return

        with open(self.data_yaml, 'r') as data_file:
            self.users = yaml.safe_load(data_file)

        if category in self.users:
            choice = input(
                f"[?] Are you sure you want to delete user '{self.users[category]['name']}' with email '{self.users[category]['email']}'? (y/n):")
            if choice.lower() == 'y':
                del self.users[category]
                with open(self.data_yaml, 'w') as data:
                    yaml.dump(self.users, data, default_style='\'"')
                print(f"[+] Login category '{category}' deleted.")
            else:
                print("[+] Deletion canceled.")
                print("[+] Existing, bye!")
        else:
            print(f"[-] Login category '{category}' not found.")

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
