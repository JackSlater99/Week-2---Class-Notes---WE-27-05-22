from modules.bank_account import *

bank_account = BankAccount("John", 500, "business")
bank_account_2 = BankAccount("Jarrod", 1000, "personal")

bank_account.pay_monthly_fee()
print(bank_account.balance)

bank_account_2.pay_monthly_fee()
print(bank_account_2.balance)