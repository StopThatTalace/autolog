import argparse
import subprocess
import yaml
import os


def current_config():
    print("[+] Your current configuration:")

    current_user = subprocess.run('git config --global user.name', shell=True, capture_output=True,
                                  text=True)
    current_mail = subprocess.run('git config --global user.email', shell=True, capture_output=True,
                                  text=True)

    print(f"[User]: {current_user.stdout.strip()}")
    print(f"[Mail]: {current_mail.stdout.strip()}")


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

                # Check if self.users is None and initialize it as an empty dictionary
                if self.users is None:
                    self.users = {}
        else:
            # If the file doesn't exist, initialize self.users as an empty dictionary
            self.users = {}

        self.users[user_category] = {
            "name": input("[+] Enter the NAME of your github account:"),
            "email": input("[+] Enter the EMAIL of your github account:")
        }

        print("[+] User created!")

        with open(self.data_yaml, 'w') as data:
            yaml.dump(self.users, data, default_style='\'"')

    def show(self):
        print("-------------------")
        print("[+] Showing logins")
        print("-------------------")
        if not os.path.exists(self.data_yaml):
            print("[-] No file available.")
        else:
            with open(self.data_yaml, 'r') as data_file:
                self.users = yaml.safe_load(data_file)

            if not self.users:
                print("[-] No logins available.")
            else:
                for category, user_info in self.users.items():
                    print(f"[{category}]: {user_info['name']} - {user_info['email']}")
                    print("-------------------")

                current_config()

    def login(self):
        category = input("[+] Enter the name of the login category you want to use: ")
        if not os.path.exists(self.data_yaml):
            print("[-] No file or no USER found.")

        else:
            with open(self.data_yaml, 'r') as data_file:
                self.users = yaml.safe_load(data_file)

            if category in self.users:
                current_user = subprocess.run(f"git config --global user.name  {self.users[category]['name']}", shell=True, capture_output=True,
                                              text=True)
                current_mail = subprocess.run(f"git config --global user.email {self.users[category]['email']}", shell=True, capture_output=True,
                                              text=True)
                print(f"[+] Logging in as {self.users[category]['name']}")
                current_config()
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

    def edit(self):
        category = input("[+] Enter the name of the login category you want to EDIT: ")

        if not os.path.exists(self.data_yaml):
            print("[-] No file or no USER found.")
            return

        with open(self.data_yaml, 'r') as data_file:
            self.users = yaml.safe_load(data_file)

        if category in self.users:
            print(f"[+] Editing user in category '{category}':")
            new_name = input(f"Enter the new NAME (current: {self.users[category]['name']}): ")
            new_email = input(f"Enter the new EMAIL (current: {self.users[category]['email']}): ")

            choice = input(
                f"[?] Are you sure you want to update user '{self.users[category]['name']}' with new name '{new_name}' and new email '{new_email}'? (y/n): ")
            if choice.lower() == 'y':
                self.users[category]['name'] = new_name
                self.users[category]['email'] = new_email
                with open(self.data_yaml, 'w') as data:
                    yaml.dump(self.users, data, default_style='\'"')
                print(f"[+] User in category '{category}' updated.")
            else:
                print("[+] Update canceled.")
                print("[+] Exiting, bye!")
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
