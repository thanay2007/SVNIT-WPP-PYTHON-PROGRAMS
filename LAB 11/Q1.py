import pandas as pd
from datetime import datetime

# a) Datetime object for Jan 15 2012
dt_a = pd.to_datetime('Jan 15 2012')
print("a) Jan 15 2012:", dt_a)

# b) Specific date and time of 9:20 pm
dt_b = pd.to_datetime('Jan 15 2012 9:20pm')
print("b) Jan 15 2012 9:20pm:", dt_b)

# c) Local date and time
dt_c = pd.to_datetime('today')
print("c) Local date and time:", dt_c)

# d) Date without time
dt_d = pd.to_datetime('today').normalize()
print("d) Date without time:", dt_d)

# e) Current date
dt_e = pd.to_datetime('today').date()
print("e) Current date:", dt_e)

# f) Time from a datetime
dt_f = pd.to_datetime('Jan 15 2012 9:20pm').time()
print("f) Time from datetime:", dt_f)

# g) Current local time
dt_g = pd.to_datetime('now').time()
print("g) Current local time:", dt_g)
