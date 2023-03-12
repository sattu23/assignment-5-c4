#Challenge 4: Implement a Banking Account

class account:
    
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
        
class savingsaccount(account):
    
    def __init__(self, title, balance,intrate):
        self.title=title
        self.balance=balance
        self.intrate=intrate
        
    def display(self):
        return (f'{self.title}  is the title, and {self.balance} is the account balance,and {self.intrate} is the interest rate' )
name=input('enter the name>>')
balance=int(input('enter your balance>>'))
intrate=int(input('enter interest rate %>>'))
obj=savingsaccount(name,balance,intrate)
print(obj.display())    