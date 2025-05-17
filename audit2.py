#!/usr/bin/env python3
import sys
import argparse

def main():
    print("Command line arguments received:")
    print(f"sys.argv: {sys.argv}")
    
    print("\nAttempting to parse arguments:")
    parser = argparse.ArgumentParser(description='Debug command line arguments')
    parser.add_argument('-d', '--directory', default='.', help='Directory to start searching')
    parser.add_argument('-i', '--ignore-file', default='fileignore', help='Path to ignore file')
    parser.add_argument('-r', '--recursive', action='store_true', help='Search recursively')
    
    try:
        args = parser.parse_args()
        print(f"Successfully parsed arguments: {args}")
    except SystemExit as e:
        print(f"SystemExit encountered with code: {e.code}")
        print("This usually means there was an error in the command line arguments")

if __name__ == "__main__":
    main()