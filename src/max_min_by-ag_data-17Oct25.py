from dataclasses import dataclass
import sys
from typing import Hashable

import pandas as pd


@dataclass(frozen=True, slots=True)
class DataClean:
    df: pd.DataFrame

    def max_by(self, id: str, val: str) -> Hashable:
        return self.df[[id, val]].max().reset_index().iloc[0, 1]

    def min_by(self, id: str, val: str) -> Hashable:
        return self.df[[id, val]].min().reset_index().iloc[0, 1]

    def gt(self, id: str, val: str, amt: int) -> str:
        return ", ".join(list(self.df[id][self.df[val] > amt]))


if __name__ == "__main__":
    aggdata = DataClean(df=pd.read_csv(sys.argv[1]))
    print(f"Highest exports: \n{aggdata.max_by('state', 'total exports')}\n")
    print(f"Lowest pork exports: \n{aggdata.min_by('state', 'pork')}\n")
    print(f"Dairy over 200: \n{aggdata.gt('state', 'dairy', 200)}\n")
