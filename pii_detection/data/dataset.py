import json
from typing import TypedDict, List
from torch.utils.data import Dataset

_all__ = ["KagglePIIDataset", "KagglePIITrainData", "KagglePIITestData"]


class KagglePIITrainData(TypedDict):
    document: int
    full_text: str
    tokens: List[str]
    trailing_whitespace: List[bool]
    labels: List[str]


class KagglePIITestData(TypedDict):
    document: int
    full_text: str
    tokens: List[str]
    trailing_whitespace: List[bool]


class KagglePIIDataset(Dataset):
    def __init__(self, data_path: str, train=True) -> None:
        super().__init__()
        with open(data_path, "r") as json_file:
            self.data: List[KagglePIITrainData | KagglePIITestData] = json.load(
                json_file
            )

    def __getitem__(self, index) -> KagglePIITrainData | KagglePIITestData:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)
