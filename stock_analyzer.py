import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

class StockData:
    def __init__(self, symbol, start_date, end_date):
        #  setters to validate and set the inputs
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self._data = None #the fetched data is gonna be stored here

    #to access the symbols from input
    @property
    def symbol(self):
        return self._symbol
    
    #to check and set the symbols from input
    @symbol.setter
    def symbol(self, symbol):
        if isinstance(symbol, str):
            self._symbol = symbol
        else:
            raise ValueError("Symbol should be a string")
        
    #same for start_date and end_date
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str):  # Validate as needed
            self._start_date = start_date
        else:
            raise ValueError("Start date should be a string")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str):  # Validate as needed
            self._end_date = end_date
        else:
            raise ValueError("End date should be a string")
        
    #this is where the data from yfinance is fetched and stored in data
    def fetch_data(self):
        self._data = yf.download(self._symbol, start=self._start_date, end=self._end_date)['Close']

    @property
    def data(self):
        return self._data


def main():
    print("Welcome to Stock Market Analyzer !")
    symbol = input("Enter stock symbol (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    # to create a StockData instance and fetch data
    stock = StockData(symbol, start_date, end_date)
    stock.fetch_data()
    # to create a TimeSeriesAnalyzer instance and calculate metrics
    analyzer = TimeSeriesAnalyzer(stock)
    average_return = analyzer.calculate_average_return()
    std_deviation = analyzer.calculate_std_deviation()
    
    #to create an AnalysisResult instance and display results
    result = AnalysisResult(stock, average_return, std_deviation)
    result.display()
    #generating a plot of the stock's price trend over the specified time period using the data provided in the StockData instance
    analyzer.plot_stock_price_trend()

if __name__ == "__main__":
    main()
