import pandas as pd


dataset = r"C:\Users\usuar\Documents\IBM\cursos_python\analyzing_data_with_python\module_1\automobile\imports-85.data"

# Load data and store in dataframe df:
df = pd.read_csv(dataset, header=None)

# Add headers to the dataframe
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


df.columns = headers


print(df.head(5))
