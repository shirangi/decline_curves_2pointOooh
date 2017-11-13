from luibeal import deck
import tempfile
import torch
import pickle


def bug0_serialization():
    a = torch.zeros(2, 2)
    with tempfile.TemporaryFile(mode='w+b') as tmp:
            torch.save(a, tmp)
            i = 41
            pickle.dump(i, tmp)
            tmp.seek(0)
            b = torch.load(tmp)
            j = pickle.load(tmp)


def bug1_serialization():
    a = torch.zeros(2, 2)
    with tempfile.TemporaryFile(mode='w+b') as tmp:            
            i = 41
            pickle.dump(i, tmp)
            torch.save(a, tmp)
            tmp.seek(0)
            j = pickle.load(tmp)
            b = torch.load(tmp)
