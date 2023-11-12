import argparse
import yaml

data_yaml = "data.yaml"

class GithubConfigTool:
    def __init__(self, data_yaml="data.yaml"):
        self.data_yaml = data_yaml
        self.users = {}

if __name__ == "__main__":
    github_tool = GithubConfigTool()
