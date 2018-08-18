# Monty-Hall Problem Simulator

## Problem

Suppose you are at a game show with three doors, one of which has a prize. 
You, as a guest, have two chances of choosing a door to win the prize. 
The first time you choose, the host eliminates one of the other doors, leaving you with two.  
*Are you better off switching or sticking to your first choice?*

## (Short) Explanation of Results


There are in fact three possible scenarios for the second round: always switching, always sticking to the first choice or choosing at random.
Provided that *n > 2* at the start, and that the host always knows where the prize is and never eliminates it, then:
 
  (1) If you always stick to your first option, you're more likely to lose, i.e. you only have a *1/n* chance of being right and *1 - 1/n* chance of being wrong
  
  (2) If you always switch, you're more likely to win, specifically *1 - 1/n* likelihood of winning

  (3) If you toss a fair coin, you have 50/50 chance of winning
  


## Running

You need python 3. See how to run by running:

```
$ python -m montyhall --help
```

Example run:

```
$ python -m montyhall --strategy switch --num-doors 100
Stats(num-games: 1000000, num-doors: 100, strategy: 'switch', success-ratio: 0.990014)
```