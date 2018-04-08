import json
import argparse


def load_data(data_path):
    with open(data_path) as file:
            text = file.read()
    return json.loads(text)


def make_pretty_json(json_data):
    pretty_print = (json.dumps(load_data(data_path), sort_keys=True, indent=6))
    return pretty_print


def parser_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    filepath = parser.parse_args()
    return filepath.path


if __name__ == '__main__':
    try:
        data_path = parser_path()
        json_data = data_path
        print(make_pretty_json(json_data))
    except FileNotFoundError:
        exit('No such file in directory')
    except ValueError:
        exit('Error. File have to be in .json format')