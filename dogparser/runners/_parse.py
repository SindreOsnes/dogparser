import argparse
import os

def parse():
    argument_parser = argparse.ArgumentParser(description='CLI interface for parsing DataEase files')
    argument_parser.add_argument('TABLE', help='The dataease table to parse, defines the logic')
    argument_parser.add_argument('SOURCE_FILE', help='The dataease file to parse')
    argument_parser.add_argument('DESTINATION_FOLDER', help='The destination directory')

    print('Hello World')