__author__ = 'MountainDoo'
__version__ = '0.1.1'
__last_modification__ = '2021-12-27'
import sys
import stock_history
import stock_comparison
import coin_history
import coin_comparison

print('\nWELCOME TO')
print('      /////   //                  //      //          //')
print('     //    /  //                  //                  //')
print('     //      /////  ////    ////  //  //  //   ////  /////  ////')
print('     ///      //   //  //  //   / // //   //      //  //   //  //')
print('      /////   //   //  //  //     ////    //   /////  //   //  //')
print('         ///  //   //  //  //     ////    //  //  //  //   //  //')
print('          //  //   //  //  //     // //   //  //  //  //   //  //')
print('     /    //  //   //  //  //   / //  //  //  //  //  //   //  //')
print('      /////   //    ////    ////  //  //  //   ////   //    ////')

def stock_menu():
    stock_selection = ''
    while stock_selection == '':
        print('\nStock Market Menu:')
        print('1) View stock history')
        print('2) Plot stock history')
        print('3) Download stock history')
        print('4) View stock comparison')
        print('5) Plot stock comparison')
        print('6) Download stock comparison')
        print('7) Back to main menu')
        print('0) Quit')
        option = input('\nSelect an option: ')
        if option == '0':
            sys.exit()
        elif option == '7':
            main_menu()
        elif option == '6':
            stock_comparison.download_stk_cmpr()
        elif option == '5':
            stock_comparison.plot_stk_cmpr()
        elif option == '4':
            stock_comparison.display_stk_cmpr()
        elif option == '3':
            stock_history.download_stk_hist()
        elif option == '2':
            stock_history.plot_stk_hist()
        elif option == '1':
            stock_history.display_stk_hist()
        else:
            print('Invalid selection.')
    return stock_selection


def coin_menu():
    coin_selection = ''
    while coin_selection == '':
        print('\nCryptocurrency Menu:')
        print('1) View coin history')
        print('2) Plot coin history')
        print('3) Download coin history')
        print('4) View coin comparison')
        print('5) Plot coin comparison')
        print('6) Download coin comparison')
        print('7) Back to main menu')
        print('0) Quit')
        option = input('\nSelect an option: ')
        if option == '0':
            sys.exit()
        elif option == '7':
            main_menu()
        elif option == '6':
            coin_comparison.download_coin_cmpr()
        elif option == '5':
            coin_comparison.plot_coin_cmpr()
        elif option == '4':
            coin_comparison.display_coin_cmpr()
        elif option == '3':
            coin_history.download_coin_hist()
        elif option == '2':
            coin_history.plot_coin_hist()
        elif option == '1':
            coin_history.display_coin_hist()
        else:
            print('Invalid selection.')
    return coin_selection

def main_menu():
    menu_selection = ''
    while menu_selection == '':
        print('\nMain Menu:')
        print('1) Stock Market Data')
        print('2) Cryptocurrency Data')
        print('0) Quit')
        option = input('\nSelect an option: ')
        if option == '0':
            sys.exit()
        elif option == '2':
            coin_menu()
        elif option == '1':
            stock_menu()
        else:
            print('Invalid selection.')
    return menu_selection


main_menu()
