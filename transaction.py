class Transaction:
    def __init__(self, sender, reciever_number, amount, reference):
        self.amoutnt = amount
        self.sender = sender
        self.reciever_number = reciever_number
        self.reference = reference
        
    def generateID(self):
        self.ID = '1010392839038'
        self.date = '2837636'
        