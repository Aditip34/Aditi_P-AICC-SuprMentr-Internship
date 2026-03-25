import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Bar Chart
df['Category'].value_counts().plot(kind='bar', title='Category Count')
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Pie Chart
df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Distribution")
plt.show()

# Histogram
df['Value'].plot(kind='hist', bins=10, title='Value Distribution')
plt.xlabel("Value")
plt.show()