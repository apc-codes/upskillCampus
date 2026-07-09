import matplotlib.pyplot as plt
import seaborn as sns

def plot_traffic(df):
    plt.figure(figsize=(10,5))
    sns.lineplot(x='Hour', y='Vehicles', data=df)
    plt.title("Traffic Flow")
    plt.savefig("images/traffic_plot.png")
    plt.show()
