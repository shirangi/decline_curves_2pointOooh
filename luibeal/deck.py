"""Training data interface"""

import torch


class Deck:
    """
    Training dataset container.

    Attributes:
        nseq: Number of production curves.
        lseq: Number of values per production curve.
        meta_sequence_names: Names of addditional data streams per production curve, ie stages of sorts,
            like perforation stage, additional wells stage etc..., also referred to as meta-sequences.
        **data** (nseq*(nmetaseq+1), lseq): Tensor containing production sequences plus meta-sequences
            so that production sequence[i] = data[i*(nmetaseq+1)], and the metasequence j corresponding to 
            sequence i is at data[i*(nmetaseq+1) + j]
    """

    def __init__(self, input, nseq):
        """
        Args:
            input: Input instance describing the input to the network.
            nseq: The number of training sequences in this deck.
        """
        self.nseq = nseq
        self.input = input
        nmetaseq = len(self.input.meta_sequence_names)
        self.data = torch.zeros(nseq * (nmetaseq + 1), input.lseq)

    def idx_sequence(self, i):
        nmetaseq = len(self.input.meta_sequence_names)
        return i * (nmetaseq + 1)

    def idx_meta_sequence(self, i, name):
        j = self.input.meta_sequence_names.index(name)
        return self.idx_sequence(i) + 1 + j

    def sequence(self, i):
        return self.data[self.idx_sequence(i)]

    def meta_sequence(self, i, name):
        return self.data[self.idx_meta_sequence(i, name)]

    def set_sequence(self, i, seq):
        self.data[self.idx_sequence(i)] = seq

    def set_meta_sequence(self, i, name, seq):
        self.data[self.idx_meta_sequence(i, name)] = seq
