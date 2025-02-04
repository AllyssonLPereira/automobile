import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot


dataset = r"C:\Users\usuar\Documents\IBM\cursos_python\analyzing_data_with_python\module_1\venv\automobile\imports-85.data"

# Add headers to the dataframegit
headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

# Load data and store in dataframe df:
df = pd.read_csv(dataset, names=headers)

# Replace "?" to NaN
df.replace("?", np.nan, inplace=True)

# Find the missing data
missing_data = df.isnull()


### Dealing with missing data by replacing it with the mean

# Calculate the mean value for 'normalized-losses' column
avg_norm_loss = df["normalized-losses"].astype('float').mean(axis=0)

# Replace "NaN" by mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Calculate the mean value for 'bore' column
avg_bore=df['bore'].astype('float').mean(axis=0)

# Replace "NaN" by mean value in "bore" column
df["bore"].replace(np.nan, avg_bore, inplace=True)

# Calculate the mean value for 'stroke' column
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)

# Replace "NaN" by mean value in "horsepower" column
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# Calculate the mean value for 'peak-rpm' column
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)

# Replace "NaN" by mean value in "peak-rpm" column
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# Check the most common type
# print(df['num-of-doors'].value_counts().idxmax()) --> "four"

df["num-of-doors"].replace(np.nan, "four", inplace=True)

# Eliminate the missing lines as this will be the target for making the prediction

# Simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# Reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


### Dealing with data types in the wrong format

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


### Data standardization

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df["city-L/100Km"] = 235/df["city-mpg"]

# replace (original value) by (original value)/(maximum value)
df["length"] = df["length"]/df["length"].max()
df["height"] = df["height"]/df["height"].max()
df["width"] = df["width"]/df["width"].max()


### Binning

df["horsepower"] = df["horsepower"].astype(int, copy=True)

plt.pyplot.hist(df["horsepower"])

# Set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)

group_names = ["Low", "Medium", "High"]

df["horsepower-binned"] = pd.cut(df["horsepower"], bins, labels=group_names, include_lowest=True)

# print(df[['horsepower','horsepower-binned']].head(20))
# print(df["horsepower-binned"].value_counts())

