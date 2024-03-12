from tokenizers import Tokenizer, Encoding

from .dataset import (
    KagglePIITrainData,
    KagglePIITestData,
)

__all__ = ["tokenize"]


def tokenize(
    tokenizer: Tokenizer, data: KagglePIITrainData | KagglePIITestData
) -> Encoding:
    encodings = tokenizer.encode(data["tokens"], is_pretokenized=True)
    return encodings
