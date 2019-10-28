import argparse
from . import flowlog_pprint


def main():
    parser = argparse.ArgumentParser(description='Pretty print AWS flow logs')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    flowlog_pprint.pprint_flowlog(args.filename)


if __name__ == '__main__':
    main()
