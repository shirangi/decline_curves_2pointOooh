"""Training data interface"""

import torch
import pickle
import fs
from fs.osfs import OSFS
import json
import shutil
import os

DATA_FNAME = 'data.bin'
META_FNAME = 'meta.json'


class Deck():
    """
    Training dataset container.

    Attributes:
        nseq: Number of production curves.
        lseq: Number of values per production curve.
        nmetaseq: Number of addditional data streams per production curve, ie stages of sorts,
            like perforation stage, additional wells stage etc..., also referred to as meta-sequences.
        **data** (nseq*(nmetaseq+1), lseq): Tensor containing production sequences plus meta-sequences
            so that production sequence[i] = data[i*(nmetaseq+1)], and the metasequence j corresponding to 
            sequence i is at data[i*(nmetaseq+1) + j]
    """

    def __init__(self, nseq, lseq, nmetaseq=0):
        """
        Args:
            nseq: Number of production curves, ie number of sequences.
            lseq: Data values per production curve, length of a single sequence.
            nmetaseq: Number of addditional data streams per production curve, ie stages of sorts,
                like perforation stage, additional wells stage etc...also referred to as meta sequences.
        """
        self.nseq = nseq
        self.lseq = lseq
        self.nmetaseq = nmetaseq
        self.data = torch.zeros(nseq * (nmetaseq + 1), lseq)

    def idx_sequence(self, i):
        return i * (self.nmetaseq + 1)

    def idx_meta_sequence(self, i, j):
        if self.nmetaseq > 0:
            return self.idx_sequence(i) + 1 + j
        return None

    def set_sequence(self, i, seq):
        self.data[self.idx_sequence(i)] = seq

    def set_meta_sequence(self, i, j, metaseq):
        self.data[self.idx_meta_sequence(i, j)] = metaseq


# TODO move to util module


def save(deck, fs_osfs):
    version = 0
    meta_data = {'version': version, 'nseq': deck.nseq, 
                 'lseq': deck.lseq, 'nmetaseq': deck.nmetaseq}
    fs_osfs.create(META_FNAME, wipe=True)
    with fs_osfs.open(META_FNAME, 'wt') as f:
        f.write(json.dumps(meta_data))
    fs_osfs.create(DATA_FNAME, wipe=True)
    with fs_osfs.open(DATA_FNAME, 'wb') as f:
        torch.save(deck.data, f)    


def load(fs_osfs):
    with fs_osfs.open(META_FNAME, 'r') as f:
        meta_data = json.load(f)
    deck = Deck(0, 0)
    deck.nseq = meta_data['nseq']
    deck.lseq = meta_data['lseq']
    deck.nmetaseq = meta_data['nmetaseq']
    with fs_osfs.open(DATA_FNAME, 'rb') as f:
        deck.data = torch.load(f)     
    return deck


def save_as(deck, dir_path):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)
    save(deck, OSFS(dir_path))


def load_from(dir_path):
    if not os.path.isdir(dir_path):
        raise IOError('Directory does not exist.')
    return load(OSFS(dir_path))
