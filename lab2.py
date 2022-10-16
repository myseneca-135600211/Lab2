#!/usr/bin/env python3


import sys

def command_line_args():
    name = str()
    phone_no = str()

    name = sys.argv[1]
    phone_no = sys.argv[2]

    print(f"Variabe1 = {name}")
    print(f"Variable2 = {phone_no}")
    print(f"Script: {sys.argv[0]}")
    print("The script and variables used are: ", sys.argv[0], name, phone_no)


if __name__ == "__main__":
    command_line_args()