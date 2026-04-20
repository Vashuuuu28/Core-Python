class bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance  = balance

    def deposit(self,amount):
        self.__deposit = amount
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = bankaccount("vashu",10000)
acc.deposit(2000)
print("current balance is: ", acc.get_balance())