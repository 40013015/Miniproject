"""Title:Bank Account Information
   Date:20/06/2021
"""
import re
import datetime


class Account:
    """
    docstring
    """

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """
            docstring
        """
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """
            docstring
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


# sub class
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


# create object a
a = Account('xyz')
print("Account balace of a is :", a.balance)
print("Name of the Account Holder:", a.holder)

# create object b
b = Account('pqr')
b.balance = 200
print("Account balace of b is:", b.balance)
print("Account balances of a and b are")
n = [acc.balance for acc in (a, b)]
print(n)
print("a deposited:", b.deposit(100))
print("b's balance is:", b.balance)
print("a withdrawn:", a.withdraw(90))
print("try to withdraw from b:", b.withdraw(90))
print("b's balance is:", b.balance)

# to check a's balance
BALANCE = getattr(a, 'balance')
print("a's balance is:", BALANCE)

# to check whether a is having deposit
DEPOSIT = hasattr(a, 'deposit')
print("Is a having deposits:", DEPOSIT)

# call deposit function and deposit money
Account.deposit(a, 1001)
print("Account balance of a is :", a.balance)
a.deposit(1000)
print("Account balance of b is :", a.balance)

# inheritance
checking = CheckingAccount('xyz')
print("xyz's deposited ammount is:", checking.deposit(10))

# Object abstraction(string conversion)
monday = datetime.date(2021, 6, 21)
print("money deposited on", str(monday))
print("xyz withdrawn:", checking.withdraw(5))
print("Interest for xyz:", checking.interest)

CHECK = bool(Account('pqr'))
print(CHECK)
if not Account('pqr'):
    print('pqr has nothing')

# creating a text file
with open('D:\\bank.txt', "w+") as f1:
    # write into text file
    for i in range(1):
        NEWLINE = "b's updated balance is" + " " + str(b.deposit(100))
        f1.write(NEWLINE)

# reading text file
with open('D:\\bank.txt', "r") as f1:
    for line in f1:
        print("written line is:", line)
        # replacing string in text file and printing replaced line
        new_line = line.replace("balance", "replaced_num")
        print("Updated line is:", new_line)

        # regular expressions
        x = re.search("replaced_num", str(new_line))  #
        if x:
            print("YES! We have a match!")
        else:
            print("No match")
        x = re.sub(" ", "9", new_line, 2)
        print(x)
        print("----------------------------")
        x = re.findall("ed", new_line)
        print(x)
        print("----------------------------")
        x = re.findall("310$", new_line)
        if x:
            print("Yes, the string ends with '310'")
        else:
            print("No match")
        print("----------------------------")
        x = re.findall("ed*", new_line)
        print(x)
        if x:
            print("Yes, there is at least one match!")
        else:
            print("No match")
f1.close()
print("end of code")
