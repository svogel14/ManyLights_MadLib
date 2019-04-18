def main():
    # 2. The below code does not work because we are referencing variables that we have not made yet
    #    A variable is powerful because we can set the variable in one place and use it in another
    #    In order for the code to run, we need to have 2 adjectives and 1 noun.
    # adjective1 = input("Adjective: ")
    # adjective2 = input("Adjective: ")
    # noun1 = input("Noun: ")
    # 3a. We now have a working madlib, but are missing 1 final noun to make it complete

    madlib = """
    A vacation is when you take a trip to some _""" + adjective1 + """_
    place with your _""" + adjective2 + """_ family. Usually you go to some 
    place that is near a/an _""" + noun1 + """_ or up a/an _"""
    # 3b. We have created the second noun, but now we need to actually use it in the madlib
    #+ noun2 + """_."""
    # The print function simply prints output into the console
    print(madlib)


# 1. Above we defined the 'main' function of our program, but in order for it to run we need to call the main function
# main()