class UserAccount: 
    def __init__(self, name, mobile_number, Dob, Pin, balance ):
        self.name  = name
        self.mobile_number  = mobile_number
        self.Dob  = Dob
        self.Pin  = Pin
        self.balance  = balance
    
    def get_detail(self):
        return f''' 
                 Your name: {self.name},
                 Mobile Number: {self.mobile_number}
                 Date Of Birth: {self.Dob}
                 PIN: {self.Pin}
                 Current Balance: {self.balance}
                '''
                
    def changePin(self):
        oldpin = input('Enter your old pin')
        if not oldpin == self.Pin:
            return 'Invalid old PIN'
        x = 1
        while x <= 3: 
            new_pin = input('Enter your old pin')
            confirm_new_pin = input('Enter your old pin')
            if not new_pin == confirm_new_pin:
              print('Pin Mismatch ')
              x += 1
            else:
                x = 4
                return 'You have successfully reset your PIN' 
            