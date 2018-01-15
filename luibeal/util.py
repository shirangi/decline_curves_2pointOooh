import torch
import pickle
import fs
from fs.osfs import OSFS
import json
import shutil
import os
from . import deck as lbdeck
from . import input as lbinput

DATA_FNAME = 'data.bin'
META_FNAME = 'meta.json'


def save(deck, fs_osfs):
    version = 0
    meta_data = {'version': version, 'nseq': deck.nseq, 
                 'lseq': deck.input.lseq, 'meta_sequence_names': deck.input.meta_sequence_names}
    fs_osfs.create(META_FNAME, wipe=True)
    with fs_osfs.open(META_FNAME, 'wt') as f:
        f.write(json.dumps(meta_data))
    fs_osfs.create(DATA_FNAME, wipe=True)
    with fs_osfs.open(DATA_FNAME, 'wb') as f:
        torch.save(deck.data, f)    


def load(fs_osfs):
    with fs_osfs.open(META_FNAME, 'r') as f:
        meta_data = json.load(f)
    input = lbinput.Input(meta_data['lseq'], meta_data['meta_sequence_names'])
    deck = lbdeck.Deck(input, meta_data['nseq'])
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
