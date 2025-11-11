#!/usr/bin/env python3

import argparse



print("Hello from the command line!!")


parser = argparse.ArgumentParser()
parser.add_argument("--name", help = "Creates a new name")
args = parser.parse_args()

if args.name:
    print(f"My name is {args.name}.")