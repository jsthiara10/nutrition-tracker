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
                print(f"You have entered {goal} as your daily calorie goal") # enter an option here to ask if they are sure/go back and edit calorie goal
                meals()
        except ValueError:
            print("You must enter a positive number e.g. 10 or 10.5")

def meals():
    global calories
    while True:
        try:
            meal = goal = float(input("Please enter calories in your first meal"))
            if meal < 0:
                print("Meal must have at least 0 calories")
                continue
            elif meal > 0:
                print(f"You have entered {meal} calories for your first meal")
                calories += meal
                print(f"You have consumed {calories} calories so far today")
        except ValueError:
            print("You must enter a number greater than 0 for calories")



# def macronutrients():





    # while True:
    #     protein = float(input("Please enter how many g of protein you would like to consume to day e.g. 150g"))
    #     if protein <=0.0:
    #         print("You must enter a valid number e.g. 10 or 0.5")



def main():
    print("Welcome to JST's Nutrition Tracker")
    goal_setter()

main() # start of the program
