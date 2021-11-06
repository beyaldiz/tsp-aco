import argparse

from utils.data import Data


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                         default="data/a280.tsp", help="Input file")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    data = Data(args.input)
    solver = None


if __name__ == "__main__":
    main()
