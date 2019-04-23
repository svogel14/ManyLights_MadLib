# File will be used to demonstrate a loop funtion
# The main function is the same as main.py, however with a different funtion to input words into our mad lib
# checkInput is a funtion we created seen below...

def main():
    adjective1 = checkInput("Adjective: ")
    adjective2 = checkInput("Adjective: ")
    noun1 = checkInput("Noun: ")
    noun2 = checkInput("Noun: ")
    pluralNoun1 = checkInput("Plural Noun: ")
    game1 = checkInput("Game: ")
    pluralNoun2 = checkInput("Plural Noun: ")
    verbing1 = checkInput("Verb ending in 'ing': ")
    verbing2 = checkInput("Verb ending in 'ing': ")
    pluralNoun3 = checkInput("Plural Noun: ")
    verbing3 = checkInput("Verb ending in 'ing': ")
    noun3 = checkInput("Noun: ")
    plant = checkInput("Plant: ")
    partOfBody = checkInput("Part of the Body: ")
    place = checkInput("A Place: ")
    verbing4 = checkInput("Verb ending in 'ing': ")
    adjective3 = checkInput("Adjective: ")
    number = checkInput("Number: ")
    pluralNoun4 = checkInput("Plural Noun: ")

    madlib = """
    A vacation is when you take a trip to some _""" + adjective1 + """_
    place with your _""" + adjective2 + """_ family. Usually you go to some 
    place that is near a/an _""" + noun1 + """_ or up a/an _""" + noun2 + """_.
    A good vacation place is one where you can ride _""" + pluralNoun1 + """_ 
    or play _""" + game1 + """_ or go hunting for _""" + pluralNoun2 + """_. I like to
    spend my time _""" + verbing1 + """_ or _""" + verbing2 + """_. When parents go on a
    vacation, they spend their time eating three _""" + pluralNoun3 + """_ a
    day, and fathers play golf, and mothers sit around _""" + verbing3 + """_
    Last summer, my little brother fell in a/an _""" + noun3 + """_ and
    got poison _""" + plant + """_ all over his _""" + partOfBody + """_. My family is going
    to go to (the) _""" + place + """_, and I will practice _""" + verbing4 + """_.
    Parents need vacations more than kids because parents
    are always very _""" + adjective3 + """_ and because they have to work
    _""" + number + """_ hours a day all year making enough _""" + pluralNoun4 + """_ to pay
    for the vacation."""
    print(madlib)

# This function we will use to interrupt inputting of a word during our madlib generation
def checkInput(wordType):
    #Save the word, so we can check what it is before we save it into the madlib
    word = input(wordType)

    # we check if the word = "!help", meaning our user needs help coming up with a word
    while word == "!help":
        # when "!help" is inputted, we call our help() function
        # then ask for the same word again, until we do NOT get "!help"
        help()
        word = input(wordType)
    return word

def help():
    helpText ="""
    -----------------------------------------------------
    To help, let's show some examples...
    Adjective: large, square, sour, slimy.
    Noun: person, bus, cat, river, toy.
    Game: Chess, Monopoly, Fortnite, Football, Tag.
    Verb ending in 'ing': Running, Swimming, Performing.

    Hope that helped!
    -----------------------------------------------------
    """
    print(helpText)

main()