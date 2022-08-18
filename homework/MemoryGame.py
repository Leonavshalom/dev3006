import random

difficulty = int(input("Please enter the how much numbers to memories:  "))


def generate_sequence():
    num_rand_list = list(range(1, difficulty+1))
    random.shuffle(num_rand_list)
    return num_rand_list


def get_list_from_user():
    for i in range(1,len(generate_sequence())):
        user_choice = input("Enter {} number: ".format(i))

print(generate_sequence())

