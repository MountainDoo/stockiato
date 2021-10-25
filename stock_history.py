import pandas_datareader as pdr
import matplotlib.pyplot as plt
from dateutil import parser
import os
import warnings
warnings.filterwarnings('ignore')

def date_diff(date1, date2):
    date1 = date1 #dt.strptime(date1, '%Y-%m-%d')
    date2 = date2 #dt.strptime(date2, '%Y-%m-%d')
    return abs((date2 - date1).days)

def valid_ticker_symbol():
    global ticker_symbol
    valid_start_date = '2021-05-01'
    valid_end_date = '2021-05-10'

    while True:
        try:
            ticker_symbol = input('Enter a Stock Ticker Symbol: ')
            stock_data = pdr.data.DataReader(ticker_symbol, 'yahoo', valid_start_date, valid_end_date)
            break
        except pdr._utils.RemoteDataError as exp:
            print('Not a valid ticker symbol, please enter a valid ticker symbol')

def inpt_stock_info():
    global start_date
    global end_date
    global ticker_symbol

    dateDiffLessThan10Days = True
    while dateDiffLessThan10Days:
        start_date = parser.parse(input('Enter a Start Date (YYYY-MM-DD): '))
        end_date = parser.parse(input('Enter an End Date (YYYY-MM-DD): '))
        date_difference = date_diff(start_date, end_date)
        if date_difference >= 10:
            dateDiffLessThan10 = False
            break
        else:
            print('The difference between the Start Date & End Date needs to be greater than 10!')
    valid_ticker_symbol()

def display_stk_hist():
    print('\n--------------------------DISPLAY STOCK HISTORY--------------------------\n')
    inpt_stock_info()
    stock_data = pdr.data.DataReader(ticker_symbol, 'yahoo', start_date, end_date)
    stock_data = stock_data.loc[:, ['Open', 'High', 'Low', 'Adj Close']]
    print(stock_data.tail())

def plot_stk_hist():
    print('\n--------------------------PLOT STOCK HISTORY--------------------------\n')
    inpt_stock_info()
    stock_data = pdr.data.DataReader(ticker_symbol, 'yahoo', start_date, end_date)
    stock_data = stock_data.loc[:, ['Open', 'High', 'Low', 'Adj Close']]
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('30 Day Adjusted Close Price')
    stock_data['Adj Close'].tail(30).plot()
    plt.show()

def download_stk_hist():
    print('\n--------------------------DOWNLOAD STOCK HISTORY--------------------------\n')
    user_profile = os.environ['USERPROFILE']
    inpt_stock_info()
    print('Downloading stock data...')
    stock_data = pdr.data.DataReader(ticker_symbol, 'yahoo', start_date, end_date)
    stock_data = stock_data.loc[:, ['Open', 'High', 'Low', 'Adj Close']]
    file_path = user_profile + '\\Desktop\\'
    file_name = ticker_symbol.upper() + '_Stock_Prices'
    file_type = '.xlsx'
    file_location = file_path + file_name + file_type
    data_source = r'file_location'
    stock_data.to_excel(file_location)
    print('Download complete.')

#display_stk_hist()
#plot_stk_hist()
#download_stk_hist()
