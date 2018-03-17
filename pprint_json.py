# -*- coding: utf-8 -*-
import json
import argparse


def load_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    filepath = parser.parse_args()
    return filepath


entered_path = load_data().path


def open_json():
    with open(entered_path) as f:
        text = f.read()
    return text


if __name__ == '__main__':
    pretty_print = json.loads(open_json())
    print (json.dumps(pretty_print, sort_keys=True, indent=6))
