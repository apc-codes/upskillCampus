import matplotlib.pyplot as plt
import seaborn as sns

def production_plot(df):
    plt.figure(figsize=(10,5))
    sns.barplot(x='State',y='Production',data=df)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/production_plot.png")
    plt.show()
