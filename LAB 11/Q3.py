import pandas as pd

asking_prices = pd.Series([25000, 32000, 18000, 42000, 29000])
fair_prices = pd.Series([28000, 30000, 20000, 40000, 28000])

good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print(good_deals)
