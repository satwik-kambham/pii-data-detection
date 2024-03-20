from tokenizers import Encoding
from transformers import AutoTokenizer

from .dataset import (
    KagglePIITrainData,
    KagglePIITestData,
)

__all__ = ["Preprocessor"]


class Preprocessor:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def preprocess(self, data: KagglePIITrainData | KagglePIITestData) -> Encoding:
        encoding = self.tokenizer.encode(data["tokens"], is_split_into_words=True)
        return encoding
