#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,

#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

#Question 1
e = [2200, 2350, 2600, 2130, 2190]

dif = [e[1] - e[0]]
print(dif)

#Question 2
print (sum(e[:3]))

#Question 3
if 2000 in e:
    # value_index = e.index(2000)
    value_index = True
else:
    value_index = None
print("Did I spend $2000 in any month:", value_index)

#Question 4
e.append(1980)
print (e)

#Question 5
# new = e[3] - 200
# e.pop(4)
# e.append(new)

# e[3] , e[5] = e[5] , e[3]
# print (e)

e[3] = e[3] - 200
print("my new expenses: ",e)
