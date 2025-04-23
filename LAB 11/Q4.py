import pandas as pd
import numpy as np

data = {
    'john': [True, False, False, True, True, False, True, False, False, True],
    'judy': [False, True, True, False, True, False, True, False, True, False]
}

df = pd.DataFrame(data)

df['party'] = df['john'] & df['judy']

df['days_til_party'] = np.nan
next_party = None

for i in range(len(df)-1, -1, -1):
    if df.at[i, 'party']:
        next_party = i
        df.at[i, 'days_til_party'] = 0
    elif next_party is not None:
        df.at[i, 'days_til_party'] = next_party - i
    else:
        df.at[i, 'days_til_party'] = np.nan

print(df)
