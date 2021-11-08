import argparse

from utils.aco import Environment
from utils.data import plot_length, plot_path, save_path


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                         default="data/rl11849.tsp", help="Input file")
    parser.add_argument('--num-ants', type=int,
                         default=10, help="Num of ants of the colony")
    parser.add_argument('--alpha', type=float,
                         default=1.0, help="Pheromone power constant")
    parser.add_argument('--beta', type=float,
                         default=1.5, help="Visibility power constant")
    parser.add_argument('--evap-rate', type=float,
                         default=0.15, help="Pheromone evaporation rate")
    parser.add_argument('--est-len', type=float,
                         default=1.0, help="Estimated tour length")
    parser.add_argument('--num-iters', type=float,
                         default=30, help="Number of iterations")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    env = Environment(args.input, args.num_ants, args.alpha, args.beta,
                        args.evap_rate, args.est_len, args.num_iters)
    env.run()
    print(env.best_path_length)
    plot_length(env.best_path_length_history)
    # plot_path(env.best_path, env.vertices)


if __name__ == "__main__":
    main()
