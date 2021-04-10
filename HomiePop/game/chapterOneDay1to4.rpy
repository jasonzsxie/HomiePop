

label chapterOneDay1to4:
    scene day one
    pause
    # Background should be ceiling of room, blue light, morning

    scene bg bedroom
    with fade

    mc "{i}How many times does this make it now?{/i}"
    mc "{i}...It doesn't matter.{/i}" 
    mc "{i}Every school is the same.{/i}"
    mc "{i}Ever since Mom decided to start searching for a better job...{/i}"
    mc "{i}I guess I should start getting ready.{/i}"

    scene bg school entrance
    with fade
    pause
    scene bg school hallway
    show dylan holding flier

    "???" "Hey! Are you in any clubs?"

    menu:                   #asks about clubs
        "Yes":
            jump club_option_one
        
        "No":
            jump club_option_two
        
        "Ignore Him":
            jump club_option_three
    
    label club_option_one:
        mc "Yes, I am."
        show dylan flier confused
        "???" "Really? I haven't seen you around here before"
        "???" "Wait, you're a new student, aren't you?"
        show dylan handing flier
        "???" "You should join the e-Gaming club!"
        jump club_end

    label club_option_two:
        mc "No, why?"
        show dylan flier happy
        "???" "Great!"
        show dylan handing flier
        "???" "Please consider joining our club."
        jump club_end

    label club_option_three:
        show dylan angry #slight problem, we don't have an image for this
        "???" "HEY!!! I KNOW YOU HEAR ME!!!"
        scene bg school hallway
        "You continue looking forward and scurry away"
        "???" "COME TO THE E-GAMING CLUB!!!"
        jump club_end

    label club_end:
        scene bg classroom whiteboard #facing whiteboard
        with fade
        pause

    show teacher happy
    "Teacher" "Good morning!"
    "Teacher" "Class, we have a new student."
    "Teacher" "Why don't you introduce yourself?"
    mc "{i}Even after counless times, I still don't know what to say...{/i}"
    mc "Hello, I'm [mc]."

    "..."
    "{i}...hehe, he's kinda cute~{/i}"
    "{i}...Who transfers this late into the school year?{/i}"
    "{i}...Looks like a dork if you ask me...{/i}"

    show teacher neutral
    "Teacher" "Alright, class, settle down now."
    show teacher pointing
    "Teacher" "[mc], why don't you take a seat next to Kelvin."

    scene bg classroom desk #facing desks
    show kelvin happy
    kel "Hi, I'm Kelvin. Nice to meet you, [mc]!"
    mc "Hello"
    kel "If you ever need help don't be afraid to ask."
    mc "Okay..."

    scene bg classroom whiteboard
    "Teacher" "We'll be continuing from our last lesson on combinations and permutations"
    "The teacher turns around and begins writing numbers on the whiteboard behind him" #gender not known yet
    "The lesson is long-winded, and the teacher's voice is mundane"

    scene bg desk side view
    show kelvin on phone
    kel "{size=-8}...dammit, my rank dropped again{/size}"
    mc "Rank?"
    mc "{i}What is he talking about? {/i}"
    show kelvin abashed
    kel "Oh, sorry. It's nothing; don't mind me."
    mc "{i} Looking at it more closely, the site he's on looks pretty familiar...{/i}"
    with hpunch
    mc "WAIT, YOU'RE GRANDMASTER?!?" 
    kel "Whoa? You know Leeg of Legions?!?"    
    mc "I've been playing for..."

    scene bg classroom whiteboard
    show teacher angry
    "Teacher" "Kelvin and [mc], you're being too loud!"
    "Teacher" "Why don't you two step out into the hallway?"

    scene bg hallway
    show kelvin embarrassed
    kel "Ahh, sorry to do this to you on your first day here; I was just excited to see that someone here actually plays LL."
    mc "Don't worry about it; it was my fault, too."
    mc "Also, what do you mean? Isn't LL a super popular game?"
    show kelvin neutral
    kel "It is, but most people here aren't interested in games. Everyone is too absorbed with studying or sports."
    mc "I see... Anyways, I'm only Diamond, and I've been playing for a long time."
    show kelvin happy
    kel "Still, diamond is pretty impressive!"
    "The two continue to discuss the game until the bell rings"

    show teacher neutral
    "Teacher" "Boys, you can come back in now. Next time, please try not to disrupt the lesson."
    "Kelvin and [mc]" "Sorry, it won't happen again."
    show teacher happy
    "Teacher" "Good to hear."

    scene bg classroom whiteboard
    "The rest of the classes pass by in a blur, and students are exiting the classroom."
    show kelvin happy
    kel "Hey [mc]! Hope your first day was alright"
    kel "Oh, I forgot to mention - every student needs to join a club."
    kel "Are there any clubs that you have in mind?"
    mc "Not really...now that I think about it, there was somebody trying to get me to join their club pretty desperately."
    show kelvin neutral
    kel "Oh, that's probably the e-Gaming club. They need one more member to officially register as a club but the deadline is coming up soon."
    mc "That sounds like a club I'd be interested in."
    kel "Well, they don't really play any competitive games."
    kel "It's basically a social club rather than a game-focused club."
    mc "Oh..."
    kel "I'm assuming you're not interested? Oh well, there are tons of established clubs here."
    kel "For example, I'm in the tennis club"
    show kelvin handing paper
    kel "Here's a full list of clubs if you want to take a look."
    hide kelvin handing paper
    mc "Hmm..."
    mc "I don't see any clubs that really interest me."
    show kelvin neutral
    kel "That's too bad..."
    hide kelvin neutral
    mc "{i}My only hobby is LL I guess...{/i}"
    mc "{i}It's a shame that the students here don't seem to know much about the game.{/i}"
    with hpunch
    mc "{i}!!!{/i}"
    mc "Hey Kelvin, about that club deadline. When is it?"
    show kelvin thinking
    kel "Hm? I think is was by the end of the week. Today is Thursday so that means..."
    mc "{i} With only one day it'll be difficult to find other people...{/i}"
    kel "Why? Got an idea for something?"
    mc "Yeah, maybe. Could I get your help with it?"
    show kelvin smile #could be same thing as kelvin happy
    kel "Of course, what is it?"
    mc "After talking with you, I realized that it felt good to share my love of LL with someone..."
    mc "So - um -"
    mc "I was thinking that we could start a LL club."
    kel "Count me in!"
    show kelvin uncertain #maybe kelvin thinking
    kel "But with only one day..."
    mc "I know it'll be hard, but I believe we can do it."
    mc "We'll find our members tomorrow."
    show kelvin smile
    kel "Okay, let's do it."
    hide kelvin smile
    "The bell rings." #add sound maybe?
    show kelvin neutral
    kel "Shoot, I better get going. Tennis practice is going to start soon."
    kel "I'll see you tomorrow [mc]."
    mc "See you tomorrow."

    scene bg neighborhood street
    with fade
    pause
    mc "{i}School was more eventful than expected...{/i}"
    mc "{i}But in a good way.{/i}"
    mc "{i}I don't know how to explain it, but I feel like I've found something that I've been searching for a long time.{/i}"
    mc "{i}It makes me happy, yet scared at the same time...{/i}"
    mc "{i}...{/i}"
    mc "{i}I hope we can find members tomorrow.{/i}"

    scene day two
    with Fade(.5, 3, .5)
    pause

    # This ends the game.

    return
