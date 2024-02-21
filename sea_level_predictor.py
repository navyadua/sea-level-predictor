import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    x = range(df['Year'][0], 2051)
    param = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y = param.slope * x + param.intercept
    plt.plot(x,y)

    # Create second line of best fit
    x = range(2000, 2051)
    paramneu = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    y = paramneu.slope * x + paramneu.intercept
    plt.plot(x,y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()