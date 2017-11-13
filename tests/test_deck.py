from luibeal import deck
from fs.osfs import OSFS
import torch
import os, shutil


def test_indices():
    nseq = 10
    lseq = 5
    deck00 = deck.Deck(nseq, lseq)
    assert deck00.data.size() == (nseq, lseq)

    nmetaseq = 5
    deck01 = deck.Deck(nseq, lseq, nmetaseq)
    assert deck01.data.size() == (nseq * (nmetaseq + 1), lseq)

    assert deck00.idx_sequence(5) == 5
    assert deck00.idx_meta_sequence(5, 0) == None

    assert deck01.idx_sequence(5) == 5 * (nmetaseq + 1)
    assert deck01.idx_meta_sequence(5, 0) == deck01.idx_sequence(5) + 1


def test_access():
    nseq = 20
    lseq = 4
    deck00 = deck.Deck(nseq, lseq)
    seq00 = torch.ones(1, lseq)
    deck00.set_sequence(0, seq00)
    assert deck00.data[0, 0] == 1
    assert deck00.data[0, lseq - 1] == 1

    nmetaseq = 5
    deck01 = deck.Deck(nseq, lseq, nmetaseq)
    deck01.set_meta_sequence(0, 2, seq00)
    assert deck01.data[3, 0] == 1


def test_serialization():
    nseq = 10
    lseq = 5
    deck00 = deck.Deck(nseq, lseq)

    tmp_path = os.path.join('.', 'tmp_testing')
    if os.path.isdir(tmp_path):
        shutil.rmtree(tmp_path)
    os.mkdir(tmp_path)
    tmp_fs = OSFS(tmp_path)
    deck.save(deck00, tmp_fs)
    deck00_loaded = deck.load(tmp_fs)
    shutil.rmtree(tmp_path)

    assert deck00_loaded.nseq == nseq
    assert deck00_loaded.lseq == lseq
    assert deck00_loaded.lseq == lseq
    assert torch.equal(deck00.data, deck00_loaded.data)
