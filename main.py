import pandas as pd

from src.preprocessing import preprocess
from src.visualization import plot_traffic
from src.forecasting import predict

df = pd.read_csv("data/traffic.csv")

df = preprocess(df)

plot_traffic(df)

predict(df)
