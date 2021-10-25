__author__ = 'MountainDoo'
__version__ = '0.1.0'
__last_modification__ = '2021-10-15'
import sys
import stock_history as stk
import stock_comparison as cmp

print('Welcome to')
print('      /////   //                  //      //          //')
print('     //    /  //                  //                  //')
print('     //      /////  ////    ////  //  //  //   ////  /////  ////')
print('     ///      //   //  //  //   / // //   //      //  //   //  //')
print('      /////   //   //  //  //     ////    //   /////  //   //  //')
print('         ///  //   //  //  //     ////    //  //  //  //   //  //')
print('          //  //   //  //  //     // //   //  //  //  //   //  //')
print('     /    //  //   //  //  //   / //  //  //  //  //  //   //  //')
print('      /////   //    ////    ////  //  //  //   ////   //    ////')

def main_menu():
    selection = ''
    while selection == '':
        print('\nMain Menu:')
        print('1) View stock history')
        print('2) Plot stock history')
        print('3) Download stock history')
        print('4) View stock comparison')
        print('5) Plot stock comparison')
        print('6) Download stock comparison')
        print('0) Quit')
        option = input('\nSelect an option: ')
        if option == '0':
            sys.exit()
        elif option == '6':
            cmp.download_stk_cmpr()
        elif option == '5':
            cmp.plot_stk_cmpr()
        elif option == '4':
            cmp.display_stk_cmpr()
        elif option == '3':
            stk.download_stk_hist()
        elif option == '2':
            stk.plot_stk_hist()
        elif option == '1':
            stk.display_stk_hist()
        else:
            print('Invalid selection.')
    return selection

main_menu()
