import pandas as pd
import numpy as np

data = np.array(['h','e','l','l','o'])
ser = pd.Series(data)
print(ser.to_string(index=False))