import pandas as pd
import numpy as np
df = pd.read_csv("laptopData.csv")

df.head()
df.info()
df.describe()
# Convert invalid Sales Amount to numeric (abc → NaN)
df["Sales Amount"] = pd.to_numeric(df["Sales Amount"], errors="coerce")

# Convert Order Date to datetime (invalid → NaT)
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Replace empty strings with NaN
df.replace("", np.nan, inplace=True)
print(df.isnull().sum())
print(df.isnull())
df.duplicated().sum()
df["Gender"] = df["Gender"].str.upper()
print(df["Gender"])
import pandas as pd
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Order Date"] = df["Order Date"].dt.strftime("%Y-%m-%d")

print(df.head())
import pandas as pd

dates = pd.date_range(start="2025-03-13", end="2025-03-20")

df = pd.DataFrame({"Date": dates})



