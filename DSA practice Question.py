expense = [2200, 2350, 2600, 2130,2190]
total_month = len(expense)

print('The feb expenses is more than january',expense[1]-expense[0])
first_q_total = expense[:3]
total = sum(first_q_total)
print('first quartor total expenses is: ',total)
print('Did i spent exactly 2000$ expense', 2000 in expense)
jun_expense = 1980
expense.append(jun_expense)
print('June of the monthly expense adde',expense)
expense[2] = expense[2]-200
print('March expense 200$ refund updated',expense)