import pandas_datareader as pdr
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser
import os
import warnings
warnings.filterwarnings('ignore')

def date_diff(date1, date2):
    date1 = date1 #dt.strptime(date1, '%Y-%m-%d')
    date2 = date2 #dt.strptime(date2, '%Y-%m-%d')
    return abs((date2 - date1).days)

def get_ticker_symbol():
    today = datetime.today().strftime('%Y-%m-%d')
    valid_start_date = '2021-05-21'
    valid_end_date = '2021-05-21'
    global list_of_ticker_symbols
    list_of_ticker_symbols = []

    while True:
        num_of_stocks = input('Enter number of stocks: ')
        if ((int(num_of_stocks) > 0) and (int(num_of_stocks) < 11)):
            break
        else:
            print('Number must be greater than 0 and less than 11.')

    for i in range(0, int(num_of_stocks)):
        while True:
            try:
                ticker_symbol = input(str(i + 1) + ') Enter ticker symbol: ')
                stock_data = pdr.data.DataReader(ticker_symbol, 'yahoo', valid_start_date, valid_end_date)
                list_of_ticker_symbols.append(ticker_symbol)
                break
            except pdr._utils.RemoteDataError as exp:
                print('Not a valid ticker symbol, please enter a valid ticker symbol')

def input_stk_info():
    global start_date
    global end_date
    global df_col

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
    get_ticker_symbol()

    print('\nColumn fields:')
    print('     1) Open')
    print('     2) High')
    print('     3) Low')
    print('     4) Adj Close')
    field_num = input('\nSelect a column field number: ')
    if field_num == '1':
        df_col = 'Open'
    elif field_num == '2':
        df_col = 'High'
    elif field_num == '3':
        df_col = 'Low'
    elif field_num == '4':
        df_col = 'Adj Close'
    else:
        print('Not a valid choice.')

def display_stk_cmpr():
    print('\n--------------------------DISPLAY STOCK COMPARISON--------------------------\n')
    input_stk_info()
    stock_data = pdr.DataReader(list_of_ticker_symbols, 'yahoo', start_date, end_date)
    stock_data = stock_data.loc[:, df_col]
    print(stock_data)

def plot_stk_cmpr():
    print('\n--------------------------PLOT STOCK COMPARISON--------------------------\n')
    input_stk_info()
    stock_data = pdr.data.DataReader(list_of_ticker_symbols, 'yahoo', start_date, end_date)
    stock_data = stock_data.loc[:, df_col]
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('30 Day ' + df_col + ' Price')
    stock_data.tail(30).plot()
    plt.show()

def download_stk_cmpr():
    print('\n--------------------------DOWNLOAD STOCK COMPARISON--------------------------\n')
    input_stk_info()
    user_profile = os.environ['USERPROFILE']
    print('Downloading stock data...')
    stock_data = pdr.data.DataReader(list_of_ticker_symbols, 'yahoo', start_date, end_date)
    stock_data = stock_data.loc[:, df_col]
    file_path = user_profile + '\\Desktop\\'
    file_name = 'Stock_Comparison'
    file_type = '.xlsx'
    file_location = file_path + file_name + file_type
    data_source = r'file_location'
    stock_data.to_excel(file_location)
    print('Download complete.')

#display_stk_cmpr()
#plot_stk_cmpr()
#download_stk_cmpr()
