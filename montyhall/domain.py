import enum

import numpy as np


class Strategy(enum.Enum):
    FIXED = 'fixed'
    SWITCH = 'switch'
    RANDOM = 'random'

    @staticmethod
    def values():
        return [e.value for e in Strategy]


class Contestant(object):
    def __init__(self, num_doors):
        self._first = np.random.randint(0, num_doors)
        self._second = None

    def first_choice(self):
        """
        First selection
        :return:
        """
        return self._first

    def second_choice(self, options):
        """
        Two alternatives are left. Which is the final choice?
        :return:
        """
        raise NotImplementedError


class RandomContestant(Contestant):
    """
    In the second round, chooses are random, disregarding the first choice
    """
    def __init__(self, num_doors):
        super(RandomContestant, self).__init__(num_doors)

    def second_choice(self, options):
        if self._second is None:
            self._second = options[np.random.randint(len(options))]
        return self._second


class FixedContestant(Contestant):
    """
    Never switches doors
    """
    def __init__(self, num_doors):
        super(FixedContestant, self).__init__(num_doors)

    def second_choice(self, options):
        return self.first_choice()


class SwitchContestant(Contestant):
    """
    Always switches doors
    """
    def __init__(self, num_doors):
        super(SwitchContestant, self).__init__(num_doors)

    def second_choice(self, options):
        a, b = options
        if a == self.first_choice():
            return b
        return a


class SimulationSummary(object):
    def __init__(self, num_games, num_doors, strategy, wins):
        self.num_games = num_games
        self.num_doors = num_doors
        self.strategy = strategy
        self.wins = wins

    def __repr__(self):
        win_ratio = self.wins/float(self.num_games)
        return "Stats(num-games: {}, num-doors: {}, strategy: '{}', success-ratio: {})".format(
            self.num_games, self.num_doors, self.strategy, win_ratio)
