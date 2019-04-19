# File will be used to demonstrate reading a file and string substitution
# Input a file called madlib_example.txt
# file contains a madlib, with words noted by underscores, i.e. _noun_

def main():
    file = open("madlib_example.txt", "r")
    text = file.read()
    print("\n-------------The File We are reading-------------")
    print(text)
    print("-------------------------------------------------\n")

    # We will place our madlib, after word substitution into this variable
    madlib = ""
    # Loop through the provided text, by each word
    for word in text.split(" "):
        # find all of our marked words, think what identifies each madlib and how you can pick them out from regular words
        # tip, python has many string funtions, utilize them here.
        ## TODO YOUR CODE HERE

            # Next we need to get the word type from our input
            # and prompt our user to input a word for madlib with the correct word type
            ## TODO YOUR CODE HERE

            # manipulate the user input to be displayed correctly as needed
            # we want to be able to identify our user inputed words easily in the final output
            ## TODO YOUR CODE HERE
            
        # after replacing the word we will need to concatenate the words back into a finished madlib
        madlib += word + " "

    # Print out the final madlib
    print("\n------------------MadLib------------------")
    print(madlib)
    print("--------------------------------------------\n")

main()