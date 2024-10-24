# Import needed libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the NYC-pop2.csv file, use 'Borough' as the index_col, and save the dataframe in a variable df
df = pd.read_csv('NYC-pop2.csv', index_col='Borough')

# Next you need to transpose df by adding the following line to our program: df1 = df.T
df1 = df.T

# Plot the graph using the dataframe df1
df1.plot()
plt.show();