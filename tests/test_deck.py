from luibeal import deck
from fs.osfs import OSFS
import torch
import os, shutil


def test_serialization():
    nseq = 10
    lseq = 5
    deck00 = deck.Deck(nseq, lseq)
    assert deck00.data.size() == (nseq, lseq)

    tmp_path = os.path.join('.', 'tmp_testing')
    if os.path.isdir(tmp_path):
        shutil.rmtree(tmp_path)
    os.mkdir(tmp_path)
    tmp_fs = OSFS(tmp_path)
    deck.save(deck00, tmp_fs)
    deck00_loaded = deck.load(tmp_fs)
    assert deck00_loaded.nseq == nseq
    assert deck00_loaded.lseq == lseq
    assert deck00_loaded.lseq == lseq
    assert torch.equal(deck00.data, deck00_loaded.data)
    shutil.rmtree(tmp_path)
