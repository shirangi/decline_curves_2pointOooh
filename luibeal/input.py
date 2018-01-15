class Input:
    """
    Describes the input to the model in terms of sequence lenght
    and number of metasequences.
    """

    def __init__(self, lseq, meta_sequence_names=[]):
        """
        Args:
            lseq: Data values per production curve, length of a single sequence.
            meta_sequence_names: Names of addditional data streams per production curve, ie stages of sorts,
                like perforation stage, additional wells stage etc...also referred to as meta sequences.
        """
        self.lseq = lseq
        self.meta_sequence_names = meta_sequence_names
