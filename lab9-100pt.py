############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

print "What is your temperature?"
temperature = int(raw_input())
while temperature >= 100:
    if temperature >= 105:
        print "You're dead!"
    elif temperature >= 102:
        print "Have you been sick within the last 24 hours? Yes or No."
        answer1 = raw_input()
        if answer1 == "Yes":
            print "You're dead!"
        else:
            print "You might not be dead!"
    elif temperature >= 100:
        print "Have you been sick within the last 24 hours? Yes or No."
        answer2 = raw_input()
        if answer2 == "Yes":
            print "Have you recently traveled to West Africa? Yes or No."
            answer3 == raw_input()