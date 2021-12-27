import pandas_datareader as pdr
import matplotlib.pyplot as plt
from dateutil import parser
import datetime
import os
import warnings
warnings.filterwarnings('ignore')

def date_diff(date1, date2):
    date1 = date1 #dt.strptime(date1, '%Y-%m-%d')
    date2 = date2 #dt.strptime(date2, '%Y-%m-%d')
    return abs((date2 - date1).days)

def get_coin_symbol():
    today = datetime.datetime.now().date()
    valid_start_date = today
    valid_end_date = today
    global list_of_coin_symbols
    list_of_coin_symbols = []

    while True:
        num_of_coins = input('Enter number of coins: ')
        if ((int(num_of_coins) > 0) and (int(num_of_coins) < 11)):
            break
        else:
            print('Number must be greater than 0 and less than 11.')

    for i in range(0, int(num_of_coins)):
        while True:
            try:
                coin_symbol = input(str(i + 1) + ') Enter coin symbol: ').upper()
                coin_symbol = coin_symbol + '-USD'
                coin_data = pdr.data.DataReader(coin_symbol, 'yahoo', valid_start_date, valid_end_date)
                list_of_coin_symbols.append(coin_symbol)
                break
            except pdr._utils.RemoteDataError as exp:
                print('Not a valid coin symbol, please enter a valid coin symbol')

def input_coin_info():
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
    get_coin_symbol()

    df_col = ''
    while df_col == '':
        print('\nColumn fields:')
        print('     1) High')
        print('     2) Low')
        print('     3) Open')
        print('     4) Close')
        field_num = input('\nSelect a column field number: ')
        if field_num == '1':
            df_col = 'High'
        elif field_num == '2':
            df_col = 'Low'
        elif field_num == '3':
            df_col = 'Open'
        elif field_num == '4':
            df_col = 'Close'
        else:
            print('Not a valid choice.')

def display_coin_cmpr():
    print('\n--------------------------DISPLAY COIN COMPARISON--------------------------\n')
    input_coin_info()
    coin_data = pdr.DataReader(list_of_coin_symbols, 'yahoo', start_date, end_date)
    coin_data = coin_data.loc[:, df_col]
    print(coin_data)

def plot_coin_cmpr():
    print('\n--------------------------PLOT COIN COMPARISON--------------------------\n')
    input_coin_info()
    coin_data = pdr.DataReader(list_of_coin_symbols, 'yahoo', start_date, end_date)
    coin_data = coin_data.loc[:, df_col]
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('30 Day ' + df_col + ' Price')
    coin_data.tail(30).plot()
    plt.show()

def download_coin_cmpr():
    print('\n--------------------------DOWNLOAD COIN COMPARISON--------------------------\n')
    input_coin_info()
    user_profile = os.environ['USERPROFILE']
    print('Downloading coin data...')
    coin_data = pdr.data.DataReader(list_of_coin_symbols, 'yahoo', start_date, end_date)
    coin_data = coin_data.loc[:, df_col]
    file_path = user_profile + (r'/Desktop/')
    file_name = 'Coin_Comparison'
    file_type = '.xlsx'
    file_location = file_path + file_name + file_type
    data_source = r'file_location'
    coin_data.to_excel(file_location)
    print('Download complete.')

#display_coin_cmpr()
#plot_coin_cmpr()
#download_coin_cmpr()
