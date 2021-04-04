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

    if mcName == "":
        $ mcName = "Marcus" #defaults name

    # Background should be ceiling of room, blue light, morning

    scene bg bedroom
    with fade

    "{i}How many times does this make it now?{/i}"
    "{i}...It doesn't matter.{/i}" 
    "{i}Every school is the same.{/i}"
    "{i}Ever since Mom decided to start searching for a better job...{/i}"
    "{i}I guess I should start getting ready.{/i}"

    scene bg school entrance
    with fade
    pause

    "???" "Hey! Are you in any clubs?"

    
    
    show troll

    

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
