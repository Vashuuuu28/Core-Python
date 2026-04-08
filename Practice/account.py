class Account:

    def __init__(self):
        self.__number = None
        self.__accountType = None
        self.__balance = None

    def get_number(self):
        return self.__number
    def set_number(self,number ):
        print("setting accout no. to")
        self.__number = number

    def get_account_type(self):
        return self.__accountType
    def set_account_type(self, account_type):
        self.__accountType = account_type

    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        self.__balance = balance

a = Account()
a.set_number("6969")
a.set_account_type("savings account")
a.set_balance("650000")
print("account no", a.get_number())
print("account type", a.get_account_type())
print("balance", a.get_balance())