# Exercise: Array DataStructure

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190

# Create a list to store these monthly expenses and using that find out,

#     1. In Feb, how many dollars you spent extra compare to January?
#     2. Find out your total expense in first quarter (first three months) of the year.
#     3. Find out if you spent exactly 2000 dollars in any month
#     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#     5. You returned an item that you bought in a month of April and
#     got a refund of 200$. Make a correction to your monthly expense list
#     based on this
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

