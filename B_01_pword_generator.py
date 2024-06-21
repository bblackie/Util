import random
import string


# Retrieves words from text file and
# puts them into a sorted list
def get_all_words():
    all_words = []
    # open file and read the content in a list

    # words from https://github.com/tabatkins/wordle-list
    with open('words.txt', 'r') as word_list:
        for line in word_list:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            all_words.append(x)

    initial_length = len(all_words)

    all_words.sort()
    return all_words


# Checks users enter an integer that is more than zero.
def int_check(question):
    error = "Please enter an integer that is more than zero"

    # ask question and loop until we get an integer more than zero
    while True:

        try:
            response = int(input("How many passwords do you want? "))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Function to generate a random password
def generate_password():
    word1 = random.choice(words)
    word2 = random.choice(words)
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    var_pword = f"{num1}{word1.title()}{num2}{word2.title()}"
    return var_pword


# Generate passwords for each student

# Get words to be used in password
words = get_all_words()

num_students = int_check("How many passwords do you need? ")
passwords = [generate_password() for _ in range(num_students)]

# Display passwords
for i, password in enumerate(passwords, start=1):
    print(f"Student {i}: {password}")
