import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime
from dateutil import parser
import os
import warnings
warnings.filterwarnings('ignore')

def date_diff(date1, date2):
    date1 = date1 #dt.strptime(date1, '%Y-%m-%d')
    date2 = date2 #dt.strptime(date2, '%Y-%m-%d')
    return abs((date2 - date1).days)

def valid_coin_symbol():
    global coin_symbol
    today = datetime.datetime.now().date()
    valid_start_date = today #'2021-05-01'
    valid_end_date = today #'2021-05-10'

    while True:
        try:
            coin_symbol = input('Enter a Coin Symbol: ')
            coin_data = pdr.data.DataReader(coin_symbol + '-USD', 'yahoo', valid_start_date, valid_end_date)
            break
        except pdr._utils.RemoteDataError as exp:
            print('Not a valid coin symbol, please enter a valid ticker symbol')

def inpt_coin_info():
    global start_date
    global end_date
    global coin_symbol

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
    valid_coin_symbol()

#High, Low, Open, Close, Volume, Adj Close
def display_coin_hist():
    print('\n--------------------------DISPLAY COIN HISTORY--------------------------\n')
    inpt_coin_info()
    coin_data = pdr.data.DataReader(coin_symbol + '-USD', 'yahoo', start_date, end_date)
    coin_data = coin_data.loc[:, ['High', 'Low', 'Open', 'Close']]
    print(coin_data)

def plot_coin_hist():
    print('\n--------------------------PLOT COIN HISTORY--------------------------\n')
    inpt_coin_info()
    coin_data = pdr.data.DataReader(coin_symbol + '-USD', 'yahoo', start_date, end_date)
    coin_data = coin_data.loc[:, ['High', 'Low', 'Open', 'Close']]
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('30 Day Close Price')
    coin_data['Close'].tail(30).plot()
    plt.show()

def download_coin_hist():
    print('\n--------------------------DOWNLOAD COIN HISTORY--------------------------\n')
    user_profile = os.environ['USERPROFILE']
    inpt_coin_info()
    print('Downloading stock data...')
    coin_data = pdr.data.DataReader(coin_symbol + '-USD', 'yahoo', start_date, end_date)
    coin_data = coin_data.loc[:, ['High', 'Low', 'Open', 'Close']]
    file_path = user_profile + (r'/Desktop/')
    file_name = coin_symbol.upper() + '_Coin_Prices'
    file_type = '.xlsx'
    file_location = file_path + file_name + file_type
    data_source = r'file_location'
    coin_data.to_excel(file_location)
    print('Download complete.')

#display_coin_hist()
#plot_coin_hist()
#download_coin_hist()
