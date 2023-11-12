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


if __name__ == "__main__":
    autolog = Autolog()
    autolog.main()
