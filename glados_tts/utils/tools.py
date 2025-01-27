import torch

from glados_tts.utils.cleaners import Cleaner
from glados_tts.utils.tokenizer import Tokenizer


def prepare_text(text: str) -> str:
    if not ((text[-1] == '.') or (text[-1] == '?') or (text[-1] == '!')):
        text = text + '.'
    cleaner = Cleaner('english_cleaners', True, 'en-us')
    tokenizer = Tokenizer()
    return torch.as_tensor(tokenizer(cleaner(text)), dtype=torch.int, device='cpu').unsqueeze(0)


def iterfile(file_path):
    with open(file_path, mode='rb') as f:
        yield from f
