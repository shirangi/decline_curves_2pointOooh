import numpy as np
import matplotlib
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import luibeal as lb
from generate import DECK_PATH


if __name__ == '__main__':
    training_deck = lb.util.load_from(DECK_PATH)
    fig, ax = plt.subplots()
    t = np.arange(training_deck.input.lseq)
    for i in range(training_deck.nseq):
        seq = training_deck.sequence(i).numpy()
        ax.plot(t, seq, 'x')
    fig_fname = os.path.join(DECK_PATH, 'training_deck.png')
    plt.savefig(fig_fname)
