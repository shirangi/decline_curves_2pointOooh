from luibeal import deck
import torch
import os, shutil


def test_indices():
    nseq = 10
    lseq = 5
    deck00 = deck.Deck(nseq, lseq)
    assert deck00.data.size() == (nseq, lseq)

    meta_sequence_names = ['a', 'b', 'c', 'd', 'e']
    deck01 = deck.Deck(nseq, lseq, meta_sequence_names)
    nmetaseq = len(meta_sequence_names)
    assert deck01.data.size() == (nseq * (nmetaseq + 1), lseq)

    assert deck00.idx_sequence(5) == 5

    assert deck01.idx_sequence(5) == 5 * (nmetaseq + 1)
    assert deck01.idx_meta_sequence(5, 'a') == deck01.idx_sequence(5) + 1


def test_access():
    nseq = 20
    lseq = 4
    deck00 = deck.Deck(nseq, lseq)
    seq00 = torch.ones(1, lseq)
    deck00.set_sequence(0, seq00)
    assert deck00.data[0, 0] == 1
    assert deck00.data[0, lseq - 1] == 1

    meta_sequence_names = ['a', 'b', 'c', 'd', 'e']
    nmetaseq = len(meta_sequence_names)
    deck01 = deck.Deck(nseq, lseq, meta_sequence_names)
    deck01.set_meta_sequence(0, 'c', seq00)
    assert deck01.data[3, 0] == 1


def test_serialization():
    nseq = 10
    lseq = 5
    meta_sequence_names = ['a', 'b', 'c', 'd', 'e']
    deck00 = deck.Deck(nseq, lseq, meta_sequence_names)

    tmp_path = os.path.join('.', 'tmp_testing')
    deck.save_as(deck00, tmp_path)
    deck00_loaded = deck.load_from(tmp_path)
    shutil.rmtree(tmp_path)

    assert deck00_loaded.nseq == nseq
    assert deck00_loaded.lseq == lseq
    assert deck00_loaded.meta_sequence_names == meta_sequence_names
    assert torch.equal(deck00.data, deck00_loaded.data)
