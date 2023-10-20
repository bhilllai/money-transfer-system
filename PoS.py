
import random


def POS(user_lst):

    stakes = []
    totalamt = 0
    for i in user_lst:
        totalamt = totalamt + i.amount + i.reward
    for i in user_lst:
        stakes.append(int((i.amount + i.reward) * 100 / totalamt))
    users = []
    for i, j in zip(user_lst, stakes):
        users += [i.name] * j

    random.shuffle(users)
    winner = random.choice(users)
    return winner
