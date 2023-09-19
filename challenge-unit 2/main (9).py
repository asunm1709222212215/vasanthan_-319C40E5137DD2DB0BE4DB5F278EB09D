"""Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. 
Include methods to deposit money, withdraw money, and display the account balance. 
Ensure that the account balance cannot be accessed directly from outside the class. 
Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality."""


class BackAccount:

  def __init__(self, account_number, account_holder_name, account_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = account_balance

  def deposit(self, amount):
    if (amount > 0):
      self.__account_balance += amount
      print("A deposited money is ₹ {} and new balance is ₹ {}".format(
          amount, self.__account_balance))
    else:
      print("invaild amount please check the amount")

  def withdraw(self, amount):
    if (amount > 0 and amount <= self.__account_balance):
      self.__account_balance -= amount
      print("Your withdraw amount is ₹ {} and current balance is ₹ {}".format(
          amount, self.__account_balance))
    else:
      print("Invaild input lplease check the amount")

  def display(self):
    print(
        "Account balance for {} (Account number # {}): Current balane is ₹ {}".
        format(self.__account_holder_name, self.__account_number,
               self.__account_balance))


Account = BackAccount(account_number="09876543211011",
                      account_holder_name="Sathishsivam",
                      account_balance=5000.0)
Account.display()
Account.deposit(300)
Account.withdraw(200)
Account.display()
