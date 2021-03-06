"""Generates funny names by randomly combining names from 2 separate lists.
*** PSEUDO CODE ***
    Load a list of first names
    Load a list of surnames
    Choose a first name at random
    Assign the name to a variable
    Choose a surname at random
    Assign the name to a variable
    Ask the user to quit or play again
    If user plays again:
        repeat
    If user quits:
        end and exit
"""


import random

if __name__ == "__main__":

    print("Welcome to the Random Name Generator")

    # lists for first & last names

    first_name = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie­Weenie'",
                  "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
                  'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
                  'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
                  'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
                  'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
                  'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
                  'Mergatroid', '"Mr Peabody"', 'Oil­Can', 'Oinks', 'Old Scratch',
                  'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
                  'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
                  "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
                  'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
                  'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
                  "Winston 'Jazz Hands'", 'Worms')

    last_name = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
                 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
                 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
                 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley­', 'Johnson',
                 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
                 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
                 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
                 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
                 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
                 'Stevens', 'Stroganoff', 'Sugar­gold', 'Swackhamer', 'Tippins',
                 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
                 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
                 'Woolysocks')

    while True:
        firstName = random.choice(first_name)

        lastName = random.choice(last_name)

        print("\n")

        print(f"{firstName} {lastName}")

        print("\n")

        try_again = input("Try Again? (press Enter else n to quit)\n")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit!")
