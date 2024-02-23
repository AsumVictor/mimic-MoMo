import os
from userAccount import UserAccount
from transaction import Transaction


def main():
    message = '''
           HELLO HAPPY CUSTOMER!
    ----------Welcome M-MoMo Application-------
    
    You have create account before you can use.
           '''

    print(message)
    print(' ')

    response = input(
        'Press 1 to continue creating an account else press any key to exist:  ')

    if not response == '1':
        return 0

    name = input('Enter your name:  ')
    dob = input('Enter your Date of Bith:  ')
    mobile_number = input('Enter your Mobile Number:  ')
    pin = input('Enter your PIN:  ')

    user = UserAccount(name, mobile_number, dob, pin)
    os.system('cls')
    quiting = False
    while not quiting:
        print('''
         1. Transfer Money
         2. MoMo Pay
         3. Airtime Bundle
         4. Allow Cashout
         5. Financial Service
         6. Wallet
   ''')

        accept_input = int(input('Waiting for choice:  '))
        workingPrompts = accept_input == 1 or accept_input == 6

        if not workingPrompts:
            print('Service under construction! Please Try another option! either 1 or 6')
        else:
            if accept_input == 1:
                os.system('cls')

                misMatch = True
                while misMatch:
                    reciever_number = input('Enter Recievers number:  ')
                    confirm_number = input('Enter the number again:  ')
                    print(' ', end='\n')
                    if reciever_number == confirm_number:
                        misMatch = False
                    else:
                        print('Number Mismtach try again!')

                amount = float(input('Enter amount to be send:  '))
                sufficient = user.validateBalance(amount)
                if not sufficient:
                    os.system('cls')
                    print('Insufficient Balance. Transaction failed!')
                else:
                    reference = input('Enter reference:  ')
                    os.system('cls')

                    print(f'''
                     You are about to send GHC {amount} to the number  {reciever_number} REF: {reference}. Kindly Confirm your PIN to continue this   transaction.
                     ''')

                    pin = input('Enter your PIN: ')
                    correctPIN = user.confirmPIN(pin)
                    if not correctPIN:
                        os.system('cls')
                        print('Wrong Pin. Transaction failed')
                    else:
                        transction = Transaction(
                            user, reciever_number, amount, reference)
                        
                        

            else:
                print('2')


main()
