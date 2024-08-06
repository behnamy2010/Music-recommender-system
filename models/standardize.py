import pandas as pd


class StandardScaler:
    def __init__(self) -> None:
        self._mean = None
        self._std = None
    

    def fit(self , df : pd.DataFrame) -> None:
        self._mean = df.mean()
        self._std = df.std()

    

    def transform(self, df : pd.DataFrame) -> pd.DataFrame:
        
        if self._mean is None or self._std is None:
            raise Exception("The scaler has not been fitted yet!")
    

        return (df - self._mean) / self._std
