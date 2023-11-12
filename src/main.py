import argparse
import yaml

data_yaml = "data.yaml"

class Autolog:
    def __init__(self, data_yaml="data.yaml"):
        self.data_yaml = data_yaml
        self.users = {}

if __name__ == "__main__":
    autolog = Autolog()
    autolog.main()
