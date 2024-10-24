# Import needed libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the NYC-pop1.csv file and plot the data of Queens
nyc_pop1 = pd.read_csv('NYC-pop1.csv', header=5)
nyc_pop1.groupby(['Year']).sum()['Queens'].plot()
plt.show();