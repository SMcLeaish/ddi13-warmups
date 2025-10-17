from dataclasses import dataclass
import sys

import pandas as pd


@dataclass
class DataClean:
    df: pd.DataFrame

    def max_by(self, id: str, val: str) -> pd.Series:
        return self.df[[id, val]].max()

    def min_by(self, id: str, val: str) -> pd.Series:
        return self.df[[id, val]].min()

    def gt(self, id: str, val: str) -> pd.Series:
        return self.df[id][self.df[val] > 200]


if __name__ == "__main__":
    aggdata = DataClean(df=pd.read_csv(sys.argv[1]))
    print(f"Highest exports: {aggdata.max_by('state', 'total exports')}")
    print(f"Lowest pork exports: {aggdata.min_by('state', 'pork')}")
    print(f"Dairy over 200: {aggdata.gt('state', 'dairy')}")
