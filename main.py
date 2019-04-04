def main():
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    pluralNoun1 = input("Plural Noun: ")
    game1 = input("Game: ")
    pluralNoun2 = input("Plural Noun: ")
    verbing1 = input("Verb ending in 'ing': ")
    verbing2 = input("Verb ending in 'ing': ")
    pluralNoun3 = input("Plural Noun: ")
    verbing3 = input("Verb ending in 'ing': ")
    noun3 = input("Noun: ")
    plant = input("Plant: ")
    partOfBody = input("Part of the Body: ")
    place = input("A Place: ")
    verbing4 = input("Verb ending in 'ing': ")
    adjective3 = input("Adjective: ")
    number = input("Number: ")
    pluralNoun4 = input("Plural Noun: ")

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



main()