import pandas as pd

from src.cleaning import clean
from src.visualization import production_plot
from src.prediction import model

df=pd.read_csv("data/crop_data.csv")

df=clean(df)

production_plot(df)

model(df)
