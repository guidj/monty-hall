import numpy as np

from montyhall import domain


def mkplayer(strategy, num_doors):
    if strategy == domain.Strategy.RANDOM.value:
        c = domain.RandomContestant(num_doors)
    elif strategy == domain.Strategy.FIXED.value:
        c = domain.FixedContestant(num_doors)
    elif strategy == domain.Strategy.SWITCH.value:
        c = domain.SwitchContestant(num_doors)
    else:
        raise RuntimeError('Unknown strategy %s' % strategy)

    return c


def play_game(strategy, num_doors):
    contestant = mkplayer(strategy, num_doors)
    prize_door = np.random.randint(0, num_doors)
    first_choice = contestant.first_choice()

    # remove all but two options, including the first choice and winning prize
    # if they match, pick another random door; otherwise, leave prize and first-choice
    if prize_door != first_choice:
        options = [first_choice, prize_door]
    else:
        while True:
            other_door = np.random.randint(0, num_doors)
            if other_door != first_choice:
                break
        options = [first_choice, other_door]

    second_choice = contestant.second_choice(options)

    return second_choice == prize_door


def simulate(num_games, num_doors, strategy):

    wins = 0
    for i in range(num_games):
        result = play_game(strategy, num_doors)

        if result:
            wins += 1

    return domain.SimulationSummary(num_games, num_doors, strategy, wins)
