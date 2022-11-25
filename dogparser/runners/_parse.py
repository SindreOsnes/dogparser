import argparse
import os
from dogparser.parsers import hund, eier, innavl, oppdretter, tyskull, utstillingsamleres, poststed, siegervinner, kull, hdstat


def parse():
    argument_parser = argparse.ArgumentParser(description='CLI interface for parsing DataEase files')
    argument_parser.add_argument('TABLE', help='The dataease table to parse, defines the logic')
    argument_parser.add_argument('SOURCE_FILE', help='The dataease file to parse')
    argument_parser.add_argument('DESTINATION_FOLDER', help='The destination directory')

    args = argument_parser.parse_args()

    # Validate the inputs
    if args.TABLE not in ['HUNDER', 'EIERE', 'INNAVL', 'OPPDRETTERE', 'TYSKULL', 'UTSTILLINGSAMLERES', 'POSTSTEDER', 'SIEGERVINNER', 'KULL', 'HDSTAT']:
        raise AssertionError(f'Table {args.TABLE} is not valid')

    if not os.path.exists(args.SOURCE_FILE+'.DBM'):
        raise FileNotFoundError(f'The source file, {args.SOURCE_FILE}, must be a valid file.')
    
    # Create the target folders
    os.makedirs(os.path.join(args.DESTINATION_FOLDER, args.TABLE), exist_ok=True)

    if args.TABLE == 'HUNDER':
        hund.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'EIERE':
        eier.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'INNAVL':
        innavl.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'OPPDRETTERE':
        oppdretter.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'TYSKULL':
        tyskull.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'UTSTILLINGSAMLERES':
        utstillingsamleres.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'POSTSTEDER':
        poststed.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'SIEGERVINNER':
        siegervinner.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'KULL':
        kull.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    elif args.TABLE == 'HDSTAT':
        hdstat.parse(args.SOURCE_FILE, os.path.join(args.DESTINATION_FOLDER, args.TABLE))

    print('Hello World')