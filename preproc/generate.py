import numpy as np
from luibeal import deck
import torch
import os


def exponential(p0, exp, t):
    return p0 * np.exp(exp * t)


def random_exponential_decline(tlim, lseq, p0_mean, exp_mean=-0.1):
    noise = 0.1
    t = np.linspace(*tlim, lseq)
    p = exponential(p0_mean, exp_mean, t) * np.random.normal(1.0, noise, t.shape)
    return torch.from_numpy(p)


if __name__ == '__main__':
    np.random.seed(41)
    nseq, lseq = 100, 50
    p0_mean = 50.0
    tlim = (0.0, 50.0)
    training_deck = deck.Deck(nseq, lseq)
    for i in range(nseq):
        training_deck.set_sequence(i, random_exponential_decline(tlim, lseq, p0_mean))
    deck_dir = os.path.join('.', 'data', 'rand_exp')
    deck.save_as(training_deck, deck_dir)
