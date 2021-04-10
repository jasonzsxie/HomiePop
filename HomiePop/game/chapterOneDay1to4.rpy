

label chapterOneDay1to4:
    window hide
    scene day one
    pause
    # Background should be ceiling of room, blue light, morning

    scene bg bedroom
    with fade
    window show

    mc "{i}How many times does this make it now?{/i}"
    mc "{i}...It doesn't matter.{/i}" 
    mc "{i}Every school is the same.{/i}"
    mc "{i}Ever since Mom decided to start searching for a better job...{/i}"
    mc "{i}I guess I should start getting ready.{/i}"

    window hide
    scene bg school entrance
    with fade
    pause
    scene bg school hallway
    pause
    show dylan holding flier
    window show

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
        "???" "Really? I haven't seen you around here before."
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
        "You continue looking forward and scurry away."
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
    mc "{i}Even after countless times, I still don't know what to say...{/i}"
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
    mc "Hello."
    kel "If you ever need help don't be afraid to ask."
    mc "Okay..."

    scene bg classroom whiteboard
    "Teacher" "We'll be continuing from our last lesson on combinations and permutations."
    "The teacher turns around and begins writing numbers on the whiteboard behind him." #gender not known yet
    "The lesson is long-winded, and the teacher's voice is mundane."

    scene bg desk side view
    show kelvin on phone
    kel "{size=-8}...dammit, my rank dropped again.{/size}"
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
    "The two continue to discuss the game until the bell rings."

    show teacher neutral
    "Teacher" "Boys, you can come back in now. Next time, please try not to disrupt the lesson."
    "Kelvin and [mc]" "Sorry, it won't happen again."
    show teacher happy
    "Teacher" "Good to hear."

    scene bg classroom whiteboard
    "The rest of the classes pass by in a blur, and students are exiting the classroom."
    show kelvin happy
    kel "Hey [mc]! Hope your first day was alright."
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
    kel "For example, I'm in the tennis club."
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
    mc "{size=+10}{i}!!!{/i}{/size}"
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
    window hide
    with Fade(.5, 1, .5)
    pause

    scene bg school entrance
    with fade
    pause
    window show
    show kelvin smile
    kel "Hey. You ready?"
    mc "Sure."
    kel "We're going to make it happen. You believe, right?"
    mc "Yeah..."
    kel "C'mon, let's go."
    mc "{i}Okay, calm down. You can do this...{/i}"

    scene bg classroom desk
    mc "{i}Alright, I'll ask the first person I see. {/i}"
    "..."
    show regina back
    mc "{i}Ok, Ok - Let's go over it one more time.{/i}"
    mc "{i}...{/i}"
    mc "{i}\"Hi, I'm [mc].\"{/i}"
    mc "{i}\"Would you like to join my club?\"{/i}"
    mc "{i}\"What is it? Oh, it's a LL club. LL is a game about...\"{/i}"
    show regina angry
    "Random Girl" "Hey! Were you staring at me?"
    mc "No! Of course not! I mean.."
    mc "I didn't mean to! - ehr - I was thinking to myself..."
    show regina neutral
    "Random Girl" "Hmph, okay."
    "Random Girl" "What were you thinking about?"
    mc "Nothing! Well, I mean, um, actually-"
    show regina smile
    "Random Girl" "It's ok, you don't have to tell me."
    "Random Girl" "Are you sure there wasn't something you wanted to say to me?"
    mc "Yea, I guess not..."
    "Random Girl" "I'll see you, then."
    mc "Bye..."
    mc "{i}Shoot! I messed up.{/i}"
    mc "{i}But it wasn't that bad, right?{/i}"

    scene bg classroom whiteboard
    "Teacher" "Alright, get your textbooks out."
    mc "{i}I guess I'll have to wait until lunch for my next shot.{/i}"

    scene bg black screen
    "..."

    scene bg cafeteria
    mc "{i}Wow. There are a ton of people here.{/i}"
    mc "{i}Good. That means there are a lot of people to ask.{/i}"
    mc "{i}Who should I ask first?{/i}"
    window hide
    scene bg cafeteria one
    show random person one
    pause
    scene bg cafeteria two
    show random person two
    pause
    scene bg cafeteria three
    show random person three
    pause
    scene bg cafeteria four
    show dylan neutral far
    pause

    window show
    mc "{i}Oh? I recognize him.{/i}"
    mc "{i}I'll start there.{/i}"
    
    scene bg cafeteria
    show dylan neutral
    mc "Hi ... I'm [mc]-"
    "???" "Oh hey, I'm Dylan"
    show dylan happy
    d "Wait, I know you!"
    d "Are you perhaps here..." with vpunch
    extend "to talk about the e-Gaming club?!?"  #i dont think we have dylan pog
    mc "Uh, about that ..."
    show dylan sad #dejected just change name of file doesn't really matter
    d "Oh..."
    mc "Sorry, I actually wanted to talk to you about a club I'm starting."
    mc "I need members for a competitive LL club."
    mc "You're in the e-Gaming club, right?"
    mc "So I was wondering if you knew anyone who would be interested..."
    show dylan thinking
    d "Hmm... Not really, sorry."
    d "In fact, we barely found our last member for the e-Gaming club."
    show dylan smile # or happy idk
    d "Good luck finding your members, though."
    mc "That's too bad..."
    mc "Thanks anyways! I'll see you around, Dylan."
    d "Bye [mc]."

    scene bg classroom desk
    mc "{i}I asked a couple more people, but nobody was really interested...{/i}"
    mc "{i}Approaching people is a lot harder than I thought.{/i}"
    mc "{i}But I think I'm making progress!{/i}"
    mc "{i}I can talk to Dylan and Kelvin without sounding completely incoherent.{/i}"
    show kelvin happy
    kel "Hey, did you manage to find anyone that was willing to join?"
    mc "Ah..."
    mc "I didn't manage to find anyone interested in joining..."
    mc "Sorry about that, even after asking for your help with something like this..."
    kel "Oh, don't worry about it! I already got 4 members!"
    with hpunch
    mc "{size=+10}WHAT??!?!{/size}" 
    mc "THANK YOU, KELVIN! YOU'RE SERIOUSLY THE BEST!"
    show kelvin smile scratching head
    kel "Haha, no worries! I have many connections with people around here~"
    kel "I'll introduce everyone to you tomorrow!"
    show kelvin happy
    kel "Also, I've already submitted a club registration to the principal."
    kel "We'll be using room F-143."
    mc "{i}Kelvin's pretty incredible...{/i}"
    mc "{i}I found it pretty hard to even approach people, but he's already gone and found enough people for me.{/i}"
    mc "{i}Without him, I don't know what I would have done...{/i}"
    kel "If you need to reach me, here's my number."
    mc "Oh thanks, here's mine as well."
    mc "{i}No way I'm telling him my mom and sister are the only ones on my contacts list.{/i}"
    show kelvin smile
    kel "Anyways, I need to get going to tennis practice now."
    kel "See you at the meeting, [mc]."
    mc "Bye, Kelvin."

    scene bg neighborhood street
    mc "{i}I can't believe that Kelvin actually managed to recruit enough members for our club.{/i}"
    mc "{i}I wonder what everyone will be like...{/i}"

    scene day three
    window hide
    with Fade(.5, 1, .5)
    pause

    scene club room
    with fade
    pause
    window show
    mc "{i}So this is the clubroom.{/i}"
    show kelvin neutral
    kel "Oh, [mc], you're already here."
    kel "Sorry to have kept you waiting."
    kel "Well, let me introduce you to everyone."
    



    # This ends the game.

    return
