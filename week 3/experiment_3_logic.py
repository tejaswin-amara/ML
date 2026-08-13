# Experiment 3: Advanced Data Visualization and Statistical Analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_analysis(df, label):
    print(f'--- Analyzing {label} ---')
    display(df.describe())
    plt.figure(figsize=(8,4))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title(f'Correlation Matrix: {label}')
    plt.show()
