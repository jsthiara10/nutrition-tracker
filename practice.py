# I want to set a calorie goal

# I want to see as a percentage of that goal, what my total calorie intake is 

# goal = 2000

# consumed = 500

# percentage = (consumed/goal) * 100

# print(f"You are {percentage}% of the way towards your daily calorie goal! ")

# # Subtraction

# subtraction = goal - consumed

# print(f"You have {subtraction} calories left to consume today. ")

# End message

# you consumed {calories} today e.g. 2000

# you successfully reached your goal of consuming 2000 calories today



###### functionality for percentage of daily target consumed ########## 


# my target is 2000 calories

# at breakfast, i consumed 500 calories

# this is 25% of my daily calorie intake

# you consumed 500 calories. you are 25% of the way towards your daily calorie intake

## practice

target = 2000
actual = 0

consumed = float(input(f"Please enter calories consumed: "))

print(f"You consumed {consumed} calories")

actual += consumed

remainder = target - actual # potentially a global variable

print(f"You have {remainder} calories left to consume")


#remainder = We need to let the user, what percentage of their daily calorie intake they still have left to consume

# before adding percentages, lets give them raw figures












# print(f"you have consumed {actual} calories so far ")

# percentage = (actual/target) * 100







# if percentage < target:
#     print(f"You have consumed {percentage}% of your daily calorie intake. You have {remainder}")

# print(f"You have consumed {percentage}% of your daily calorie intake ")