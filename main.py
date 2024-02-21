from userAccount import UserAccount

def main():
 message  = '''
           HELLO HAPPY CUSTOMER!
    ----------Welcome M-MoMo Application-------
    
    You have create account before you can use.
           '''
           
 print(message)
 print(' ')

 response = input('Press 1 to continue creating an account else press any key to exist')

 if not response == '1':
    return 0

 quiting = False
 while not quiting:
     print(' Yes')
    
main()

