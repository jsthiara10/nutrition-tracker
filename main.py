# Purpose of the nutrition tracker:

# the user sets a calorie goal/macronutrient goal e.g. 150g protein/day

# Please enter a meal
# Meal name = breakfast or meal 1
# Meal time = 10am
# Meal description = 2 eggs and whole wheat toast
# Meal calories = 
# Meal macros = 

# you are 10% of your way towards your protein goal (e.g. consumed 15g, 135g more to go)
# Record another meal?
# If 'N' - Congratulations! You hit/exceeded your protein goal for today. Keep it up!
#or, Sorry, you did not hit your protein goal for today. Don't give up though, try adding healthier choices e.g. chicken, greek yogurt


# we need a list that takes the calorie goal
# we should p

calories = 0

def goal_setter():
    print("Select which of the following nutrition goals you would like to achieve today")
    print("1. Calories")
    print("2. Exit Program")

    while True:
        try:
            goal = int(input("Please enter the number of your choice e.g. 1: "))
            if goal == 1:
                calorie_goal()
            elif goal == 2:
                print("Exiting program. Goodbye! ")
                break
        except ValueError:
            print("Please enter a number e.g. 1 for Calories") 
    
        break

def calorie_goal():
    global calories
    while True:
        try:
            goal= float(input("Please enter your calorie goal for today e.g. 2000: "))
            if goal <0:
                print("Calorie goal cannot be less than 0 Calories")
                continue
            elif goal >=0:
                confirmation = input(f"You have entered {goal} as your daily calories. Are you sure? Yes or No? ").strip().lower()
                if confirmation == "yes":
                    print(f"Your calorie goal is set to {goal} calories. ")
                    meals(goal)
                    return goal # ends the execution of the function
                elif confirmation == "no":
                    print("Please enter your updated calorie goal. ")
                    continue
                else:
                    print("Invalid input. Please enter Yes or No. ")
        except ValueError:
            print("You must enter a positive number e.g. 10 or 10.5")
        break

def meals(goal):
    global calories
    while True:
        try:
            meal = float(input("Please enter calories in your meal: "))
            if meal < 0:
                print("Meal must have at least 0 calories")
                continue
            elif meal > 0:
                confirmation = input(f"You have entered {meal} as calories for your meal. Are you sure? Please enter yes or no" ).strip().lower()
                # conditional within a conditional
                if confirmation == "yes":
                    print(f"You have confirmed {meal} calories for your first meal")
                    calories += meal
                    remainder = goal - calories # variable which records remainder of daily calorie target
                    percentage = (calories/goal) * 100
                    print(f"You have consumed {calories} calories so far today. This is {percentage}% of your daily calorie goal. You have {remainder} calories left to consume today. ") # added remainder calories to this print statement
                else:
                    print("Calories not recorded. Please re-enter calories for your meal e.g. 200")
                    continue
            # new conditional asking them if they wish to record another meal:
                another_meal = input("Would you like to log another meal. Yes or No? ") # notice this is still under the elif meal > 0 condition. we only ask the user to log another meal if they have logged their first meal
                if another_meal == "yes":
                    continue
                elif another_meal == "no":
                    print("Thank you for logging your calories for today! ")
                    break # exit this loop
                else:
                    print("Invalid input. Please enter yes or no")
        except ValueError:
            print("You must enter a number greater than 0 for calories")


def main():
    global calories
    print("Welcome to JST's Nutrition Tracker")
    goal_setter()
    print(f"You consumed {calories} calories today")

main() # start of the program
