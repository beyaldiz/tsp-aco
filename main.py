import argparse

from utils.aco import Environment
from utils.data import plot_length


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                         default="data/rl11849.tsp", help="Input file")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    env = Environment(args.input, 10, 1.0, 1.5, 0.15, 1000000.0, 10)
    env.run()
    print(env.best_path_length)
    plot_length(env.best_path_length_history)


if __name__ == "__main__":
    main()
