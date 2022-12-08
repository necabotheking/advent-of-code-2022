#     ---Advent of Code---

# --- Day 1: Calorie Counting ---

# Santa's reindeer typically eat regular reindeer food, but they need a lot of 
# magical energy to deliver presents on Christmas. For that, their favorite 
# snack is a special type of star fruit that only grows deep in the jungle. 

# The Elves have brought you on their annual expedition to the grove 
# where the fruit grows.

# To supply enough magical energy, the expedition needs to retrieve a 
# minimum of fifty stars by December 25th. 
# Although the Elves assure you that the grove has plenty of fruit, 
# you decide to grab any fruit you see along the way, just in case.

# Collect stars by solving puzzles. 
# Two puzzles will be made available on each day in the Advent calendar; 
# the second puzzle is unlocked when you complete the first. 
# Each puzzle grants one star. Good luck!

# The jungle must be too overgrown and difficult to 
# navigate in vehicles or access from the air; the Elves' expedition
# traditionally goes on foot. 

# As your boats approach land, the Elves begin taking 
# inventory of their supplies. 

# One important consideration is food - in particular, 
# the number of Calories each Elf is carrying (your puzzle input).

# The Elves take turns writing down the number of Calories contained by the 
# various meals, snacks, rations, etc. that they've brought with them,
#  one item per line. 
 
#  Each Elf separates their own inventory from the previous 
#  Elf's inventory (if any) by a blank line.

# For example, suppose the Elves finish writing their items' 
# Calories and end up with the following list:

# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000


#     ---Part One---
# Find the Elf carrying the most Calories. 
# #How many total Calories is that Elf carrying?

def txt_to_calorie_lst(txt_file):
    """
    Creates a list of lists of calories each Elf is carrying.

    Inputs:
        txt_file (string): File path of the txt file 

    Returns: (lst) List of lists with each list having the calories
        that each elf is holding
    """
    with open(txt_file) as day_1:
        calorie_lst = [section.split() for section in day_1.read().split('\n\n')]
        day_1.close()
    return calorie_lst

def sum_and_sort(calorie_lst):
    """
    Finds the total calories of each list in the calorie list
    
    Inputs:
        calorie_lst (lst): List of lists

    Returns: (lst) a sorted list of calorie sums in descending order
    
    """
    sum_calories = []

    for value in calorie_lst:
        calorie = list(map(int, value))
        sum_calories.append(sum(calorie))
        final_sum = sorted(sum_calories, reverse=True)
    return final_sum


def find_top_n(final_sum, n):
    """
    Finds the top n calories in a list of lists of calories

    Inputs:
        final_sum (lst): list of calorie sums
        n (int): top n calories to search for

    Returns: (int) the sum of the top n calories that elves are carrying
    """
    return sum(final_sum[0:n])

def solve_part_one():
    """
    Solves Advent of Code part one
    
    Returns: (int) max calories that one elf is carrying
    """
    txt_file = "data/day_1.txt"
    calorie_lst = txt_to_calorie_lst(txt_file)
    final_sum = sum_and_sort(calorie_lst)

    return find_top_n(final_sum, 1)

#     ---Part Two---
# By the time you calculate the answer to the Elves' question, 
# they've already realized that the Elf carrying the most Calories 
# of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know 
# the total Calories carried by the top three Elves carrying the most Calories. 
# That way, even if one of those Elves runs out of snacks, they still have 
# two backups.

# In the example above, the top three Elves are the fourth Elf 
# (with 24000 Calories), then the third Elf (with 11000 Calories), 
# then the fifth Elf (with 10000 Calories). 
# The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?

def solve_part_two():
    """
    Solves Advent of Code part one
    
    Returns: (int) sum of calories that the top 3 elves are carrying
    """
    txt_file = "data/day_1.txt"
    calorie_lst = txt_to_calorie_lst(txt_file)
    final_sum = sum_and_sort(calorie_lst)

    return find_top_n(final_sum, 3)