import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # First line of best fit (all data)
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    sea_level_all = intercept_all + slope_all * years_all
    ax.plot(years_all, sea_level_all, 'r', label='Fit all data')

    # Second line of best fit (from year 2000)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = np.arange(2000, 2051)
    sea_level_2000 = intercept_2000 + slope_2000 * years_2000
    ax.plot(years_2000, sea_level_2000, 'green', label='Fit 2000 onwards')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save figure
    fig.savefig('sea_level_plot.png')
    return fig