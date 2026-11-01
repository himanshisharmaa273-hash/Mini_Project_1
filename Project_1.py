'''STUDENT MONTHLY BUDGET ANALYZER'''

#input student name
stuentName=input("Enter Student Name:")

#student's Monthly income
monthlyIncome=float(input("Enter Monthly Income($):"))

#student's Food expenses
foodExpenses=float(input("Enter Food Expenses($):"))

#student's Travel Expense
travelExpenses=float(input("Enter Travel Expenses($):"))

#student's Study materials expense
studyMaterials=float(input("Enter Expenses on Study Materials($): "))

#student's internet/mobile expense
internetExpenses=float(input("Enter Mobile/Internet Expenses($):"))

#other expenses like movie, clothes...etc
otherExpenses=float(input("Enter Other Expenses($):"))

#Total Expenses
totalExpenses = (foodExpenses + travelExpenses + studyMaterials + internetExpenses + otherExpenses)

#Remaining balance
remainingBalance = (monthlyIncome - totalExpenses)

#Savings Rate
saving = (remainingBalance/monthlyIncome)*100

print("="*30)
print("\n MONTHLY BUDGET REPORT")
print("="*30)

print(f"Student: ${stuentName}")
print(f"Monthly Income: ${monthlyIncome}")
print(f"Food: ${foodExpenses}")
print(f"Travel: ${travelExpenses}")
print(f"Study Materials: ${studyMaterials}")
print(f"Mobile/Internet: ${internetExpenses}")
print(f"Other: ${otherExpenses}")
print(f"Total Expenses: ${totalExpenses}")
print(f"Remaining Balance: ${remainingBalance}")
print(f"Savings Rate: {saving}%")