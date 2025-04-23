import pandas as pd

concerts = pd.DataFrame({
    'artist': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C'],
    'venue': ['X', 'Y', 'X', 'Z', 'X', 'Y', 'Y', 'X'],
    'date': pd.to_datetime(['2023-01-15', '2023-01-20', '2023-02-10', 
                           '2023-02-15', '2023-02-20', '2023-03-05',
                           '2023-03-10', '2023-03-15'])
})

concerts['year_month'] = concerts['date'].dt.to_period('M')
cross = pd.MultiIndex.from_product([concerts['artist'].unique(), 
                                  concerts['venue'].unique()], 
                                 names=['artist', 'venue'])

counts = concerts.groupby(['year_month', 'artist', 'venue']).size().unstack(['artist', 'venue'])
counts = counts.reindex(columns=cross, fill_value=0)

print(counts)
