import argparse
import yaml

data_yaml = "data.yaml"

class Autolog:
    def __init__(self, data_yaml="data.yaml"):
        self.data_yaml = data_yaml
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

if __name__ == "__main__":
    autolog = Autolog()
    autolog.main()
