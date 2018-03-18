import json
import argparse


def load_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    filepath = parser.parse_args()
    with open(filepath.path) as f:
        text = f.read()
        pretty_loads = json.loads(text)
    return pretty_loads


def pretty_print_json():
    pretty_print = (json.dumps(load_data(), sort_keys=True, indent=6))
    return pretty_print


if __name__ == '__main__':
    try:
        print (pretty_print_json())
    except IndexError:
        print ('Type in a path to the .json file')
        exit()
    except FileNotFoundError:
        print ('No such file in directory')
        exit()
    except ValueError:
        print ('Error. File have to be in .json format')
        exit()
