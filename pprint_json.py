import json
import argparse


def load_data(myfile):
    try:
        with open(myfile) as file:
            text = file.read()
        return json.loads(text)
    except IndexError:
        #exit('Type in a path to the .json file')
        None
    except FileNotFoundError:
        #exit('No such file in directory')
        None
    except ValueError:
        #exit('Error. File have to be in .json format')
        None


def pretty_json(json_data):
    pretty_print = (json.dumps(load_data(myfile), sort_keys=True, indent=6))
    return pretty_print


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    filepath = parser.parse_args()
    myfile = filepath.path
    json_data = load_data(myfile)
    print(pretty_json(json_data))