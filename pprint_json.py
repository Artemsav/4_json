import json
import argparse


def load_data():
    with open(parser_data().path) as file:
        text = file.read()
        pretty_loads = json.loads(text)
    return pretty_loads


def pretty_json():
    pretty_print = (json.dumps(load_data(), sort_keys=True, indent=6))
    return pretty_print


if __name__ == '__main__':

    def parser_data():
        parser = argparse.ArgumentParser()
        parser.add_argument('path')
        filepath = parser.parse_args()
        return filepath

    try:
        print (pretty_json())
    except IndexError:
        exit('Type in a path to the .json file')
    except FileNotFoundError:
        exit('No such file in directory')
    except ValueError:
        exit('Error. File have to be in .json format')
