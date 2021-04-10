# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen") define a character
define mc = Character("[mcName]")
define d = Character("Dylan")
define e = Character("Ethan")
define ja = Character("Jacob")
define jo = Character("Josh")
define kel = Character("Kelvin")
define kev = Character("Kevin")
define kr = Character("Kristella")
define ma = Character("Maryanne")
define mi = Character("Micaiah")
define r = Character("Regina")
define t = Character("Tiffany")




# The game starts here.

label start:
   
    $ mcName = renpy.input("What is your name?", length=32)
    $ mcName = mcName.strip() #gets rid of unnecessary white space
    while mcName == "":
        if mcName == "":
            $ mcName = renpy.input("Please enter a name", length=32)
            $ mcName = mcName.strip() #gets rid of unnecessary white space

    jump chapterOneDay1to4

    # This ends the game.

    return
