import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

class TimeSeriesAnalyzer:
    def __init__(self, stock_data):
        self._stock_data = stock_data
    # Calculating the daily percentage change in stock prices
    def calculate_daily_returns(self):
        return (self._stock_data.data.pct_change() * 100).dropna() #it returns a one dimentional array that belongs to pandas libaray
    #it gives users an overall trend of the stock's performance over the specified time period.
    def calculate_average_return(self):
        daily_returns = self.calculate_daily_returns()
        return np.mean(daily_returns) #we're using numpy here
    #It measures the volatility or risk associated with the stock's daily price changes
    def calculate_std_deviation(self):
        daily_returns = self.calculate_daily_returns()
        return np.std(daily_returns) #numpy here

    def plot_stock_price_trend(self):
        #This function from the matplotlib.pyplot library is used to create a line plot.
        plt.plot(self._stock_data.data.index, self._stock_data.data) 

        #plt.xlabel sets the label for the x-axis of the plot
        plt.xlabel('Date')
        
        #plt.ylabel sets the label for the y-axis of the plot
        plt.ylabel('Stock Price')
        #plt.title sets the title of the plot 
        plt.title('Stock Price Trend')

        # plt.xticks sets the positions and labels for the tick marks on the x-axis
        plt.xticks(rotation=45)
        #plt.tight_layout automatically adjusts the spacing between subplots to make sure everything fits within the figure area
        plt.tight_layout()
        #savefig saves the current figure to a file as an image
        plt.savefig('img/stock_price_trend.png')
        #Displays the plot on the screen
        plt.show()