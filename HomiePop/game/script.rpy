﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen") define a character
define mc = Character("[mcName]")


# The game starts here.

label start:
   
    $ mcName = renpy.input("What is your name?", length=32)
    $ mcName = mcName.strip() #gets rid of unnecessary white space

    if mcName == "":
        $ mcName = "Insert Name Here" #insert better name here

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show troll

    mc "My name is [mcName]!"

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
