import random as rand
import datetime as dt

class BasicAccount:
    
    accountNumber = 0

    def __init__(self,acName:str,openingBalance:float):
        self.name = acName
        self.balance = openingBalance
        self.cardNum = str()
        self.cardExp = (int,int)
        BasicAccount.accountNumber = BasicAccount.accountNumber + 1
        self.acNum = str(BasicAccount.accountNumber)
        self.account_status = True

    def __str__(self):
        return f'Name {self.name}\nAccount Number {self.acNum}\nBalance {self.balance}\nCard Number {self.cardNum}\nExpiry Date{self.cardExp}'
    
    def deposit(self,amount):
        if self.account_status:
            if amount>0:
                self.balance += amount
                print(f'{self.name} deposited {amount} £. New balance: {self.balance} £')
    
    def withdraw(self,amount):
        if self.account_status:
            if amount < self.balance:
                self.balance -= amount
                print(f'{self.name} withdrawn {amount} £. New balance: {self.balance} £')
            else:
                print(f'Cannot withdraw {amount} £')
    def getAvailableBalance(self):
        return self.balance

    def getBalance(self):
        return self.balance

    def printBalance(self):
        print("Account Summary")
        print(f"Name : {self.name}")
        print(f"Account : {self.acNum}")
        print("Balance: {}£".format(self.getAvailableBalance()))
        if self.account_status:
            print("Account status : Open")
        else:
            print("Account status : Closed")

    def getName(self):
        return self.name
    def getAcNum(self):
        return self.acNum

    def issueNewCard(self):
        if self.account_status:
            currentDT = dt.datetime.now()
            exp_year = currentDT.year + 3
            exp_month = currentDT.month
            self.cardExp = (exp_month, exp_year)
            self.cardNum = str(rand.randint(1000, 10000)) +'-'+ str(rand.randint(1000, 10000)) +'-'+ str(rand.randint(1000, 10000)) + '-'+str(rand.randint(1000, 10000))
        else:
            print("Card cannot be issued as account is Closed")

class PremiumAccount(BasicAccount):
    def __init__(self,acName:str,openingBalance:float,initialOverdraft:float):
        self.overdraft = True
        self.overdraftLimit = initialOverdraft
        # invoking the __init__ of the parent class
        BasicAccount.__init__(self,acName, openingBalance)
    

    def setOverdraftLimit(self,newLimit:float):
        if self.account_status:
            self.overdraft = True
            if self.balance>=0:
                self.overdraftLimit = newLimit
                print(f"New overdraft limit for {self.name} Account number {self.acNum} is {self.overdraftLimit} ")
            else:
                print(f"Overdraft limit cannot be updated as account balance is: {self.balance}")
                print(f"Deposit {self.balance*(-1)} to set new overdraft limit of {newLimit}")
        else:
            print("Account is closed")

    def getAvailableBalance(self):
        if self.overdraft == True:
            return self.balance+self.overdraftLimit
        else:
            super().getAvailableBalance()

    def printBalance(self):
        if self.overdraft == True:
            print("Account Summary")
            if self.overdraft == True:
                print(f"Name : {self.name}")
                print(f"Account : {self.acNum}")
                print("Balance: {} £".format(self.balance))
                print("Overdraft balance: {} £".format(self.overdraftLimit))
                print(f"Available balance : {self.getAvailableBalance()} £")
                print("Account status: Open")
        else:
            super().printBalance()

    def withdraw(self,amount):
        if self.account_status:
            if self.overdraft==True:
                if amount>self.balance + self.overdraftLimit:
                    print(f'Cannot withdraw {amount} £')
                elif amount>=self.balance and amount<self.overdraftLimit + self.balance:
                    temp = amount - self.balance
                    self.overdraftLimit = self.overdraftLimit - temp
                    self.balance = -(temp)
                    print(f'{self.name} withdrawn {amount} £. New balance: {self.balance} £ and New overdraft limit {self.overdraftLimit}')
            else:
                super().withdraw(amount)

    def closeAccount(self):
        if self.balance>=0:
            self.printBalance()
            self.withdraw(self.balance)
            self.account_status = False
            self.overdraftLimit = 0
            self.overdraft = True
            self.balance = 0
            self.printBalance()
            print("Account closed successfully")
            return True
        else:
            print(
                f'Can not close account due to customer being overdrawn by £{self.balance}')
            return False
    def __str__(self):
            return f'Name {self.name}\nAccount Number {self.acNum}\nBalance {self.balance}\nCard Number {self.cardNum}\nExpiry Date {self.cardExp}\nOverdraft balance {self.overdraftLimit}\n'

    
        




if __name__ == "__main__":
    print("=="*20+"Testing"+"=="*20)
    

    #Creating First Account
    a1 = PremiumAccount("Mike",4000,2000)
    a1.issueNewCard()#Issuing card
    print(a1)#calling __str__() method
    a1.deposit(1000)
    a1.withdraw(1500)
    a1.withdraw(4000)
    a1.printBalance()
    a1.setOverdraftLimit(4000)
    a1.printBalance()
    print('-'*50)

    #Creating Second Account
    a2 = PremiumAccount("Stella",5000,2500)
    a2.issueNewCard()#Issuing card
    print(a2)  # calling __str__() method
    a2.deposit(100)
    a2.withdraw(1500)
    a2.withdraw(7000)
    a2.printBalance()
    a2.setOverdraftLimit(4000)
    a2.closeAccount()
    a2.deposit(3000)
    a2.setOverdraftLimit(4000)
    a2.closeAccount()
    print('-'*50)
