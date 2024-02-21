from userAccount import UserAccount

def main():
 message  = '''
           HELLO HAPPY CUSTOMER!
    ----------Welcome M-MoMo Application-------
    
    You have create account before you can use.
           '''
           
 print(message)
 print(' ')

 response = input('Press 1 to continue creating an account else press any key to exist:  ')

 if not response == '1':
    return 0
 
 name = input('Enter your name:  ')
 dob = input('Enter your Date of Bith:  ')
 mobile_number = input('Enter your Mobile Number:  ')
 pin = input('Enter your PIN:  ')
 
 user = UserAccount(name, mobile_number, dob, pin)
 
 print('------Your Account details-------')
 print(user.get_detail())
 print('-------------------------------')


 quiting = False
 while not quiting:
     x = 1
     # create an account
     # after account bring menu
     
    
main()

