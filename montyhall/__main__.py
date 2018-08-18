import argparse

from montyhall import domain
from montyhall import simulation


def parse_args():

    arg_parser = argparse.ArgumentParser(description='Monty-Hall simulator')

    arg_parser.add_argument('--num-games', type=int, help='Number of games to simulate', required=False, default=10**6)
    arg_parser.add_argument('--strategy', choices=domain.Strategy.values(), required=True)
    arg_parser.add_argument('--num-doors', type=int, help='Number of doors', required=False, default=3)

    args = arg_parser.parse_args()

    if args.num_doors < 3:
        raise RuntimeError('--num-doors should be at least 3')

    return args


def main(num_games, strategy, num_doors):

    summary = simulation.simulate(num_games, num_doors, strategy)
    print(summary)


if __name__ == '__main__':

    args = parse_args()
    main(args.num_games, args.strategy, args.num_doors)
