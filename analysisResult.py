
class AnalysisResult:
    def __init__(self, stock_data, average_return, std_deviation):
        self._stock_data = stock_data 
        self._average_return = average_return
        self._std_deviation = std_deviation
    # Display analysis results
    def display(self):
        print("\nAnalysis Results:")
        print(f"Stock Symbol: {self._stock_data.symbol}")
        print(f"Time Period: {self._stock_data._start_date} to {self._stock_data._end_date}")
        print(f"Average Daily Return: {self._average_return:.2f}%")
        print(f"Standard Deviation: {self._std_deviation:.2f}")

    @property
    def stock_data(self):
        return self._stock_data

    @property
    def average_return(self):
        return self._average_return

    @property
    def std_deviation(self):
        return self._std_deviation