import argparse
import os

def parse():
    argument_parser = argparse.ArgumentParser(description='CLI interface for parsing DataEase files')
    argument_parser.add_argument('TABLE', help='The dataease table to parse, defines the logic')
    argument_parser.add_argument('SOURCE_FILE', help='The dataease file to parse')
    argument_parser.add_argument('DESTINATION_FOLDER', help='The destination directory')

    args = argument_parser.parse_args()

    # Validate the inputs
    if args.TABLE not in ['HUNDER']:
        raise AssertionError(f'Table {args.TABLE} is not valid')

    if not os.path.exists(args.SOURCE_FILE+'.DBM'):
        raise FileNotFoundError(f'The source file, {args.SOURCE_FILE}, must be a valid file.')
    
    # Create the target folders
    os.makedirs(os.path.join(args.DESTINATION_FOLDER, args.TABLE), exist_ok=True)

    print('Hello World')