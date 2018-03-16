#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import argparse
import sys

def load_data():
    filepath= argparse.ArgumentParser()
    filepath.add_argument('path', type=argparse.FileType(mode='r', bufsize=-1,encoding="utf-8",errors=None), help='Type in a path!')
    """with open(filepath, 'r') as filepath:
        filepath.read()"""
    return filepath

def pretty_print_json():

    namespace = load_data().parse_args(sys.argv[1:])
    text = namespace.path.read()
    return text



if __name__ == '__main__':
    #filepath=load_data()
    #namespace=filepath.parse_args(sys.argv[1:])
    #text=namespace.path.read()
    newone=json.loads(pretty_print_json())
    print (json.dumps(newone, sort_keys=True, indent=6))
    #print (json.dumps({pretty_print_json()}))
    #print (json.loads(pretty_print_json()))