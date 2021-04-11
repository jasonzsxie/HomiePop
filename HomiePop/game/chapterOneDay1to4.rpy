label chapterOneDay1to4:
    $ whoFirst = ""
    $ whoSecond = ""
    $ whoThird  = ""
    $ girlsTalkedTo = 0
    window hide
    scene day one
    pause
    # Background should be ceiling of room, blue light, morning

    scene bg bedroom
    with fade
    pause(.5)
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
    with fade
    pause(.5)
    show dylan holding flier
    pause(.25)
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
        pause(.25)
        "???" "Really? I haven't seen you around here before."
        "???" "Wait, you're a new student, aren't you?"
        show dylan handing flier
        pause(.25)
        "???" "You should join the e-Gaming club!"
        jump club_end

    label club_option_two:
        mc "No, why?"
        show dylan flier happy
        pause(.25)
        "???" "Great!"
        show dylan handing flier
        pause(.25)
        "???" "Please consider joining our club."
        jump club_end

    label club_option_three:
        show dylan angry #slight problem, we don't have an image for this
        pause(.25)
        "???" "HEY!!! I KNOW YOU HEAR ME!!!"
        scene bg school hallway
        pause(.25)
        "You continue looking forward and scurry away."
        "???" "COME TO THE E-GAMING CLUB!!!"
        jump club_end

    label club_end:
        scene bg classroom whiteboard #facing whiteboard
        with fade
        pause

    show teacher happy
    pause(.25)
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
    pause(.25)
    "Teacher" "Alright, class, settle down now."
    show teacher pointing
    pause(.25)
    "Teacher" "[mc], why don't you take a seat next to Kelvin."

    scene bg classroom desk #facing desks
    pause(.5)
    show kelvin happy
    pause(.25)
    kel "Hi, I'm Kelvin. Nice to meet you, [mc]!"
    mc "Hello."
    kel "If you ever need help, don't be afraid to ask."
    mc "Okay..."

    scene bg classroom whiteboard
    pause(.5)
    "Teacher" "We'll be continuing from our last lesson on combinations and permutations."
    "The teacher turns around and begins writing numbers on the whiteboard behind him." #gender not known yet
    "The lesson is long-winded, and the teacher's voice is mundane."

    scene bg desk side view
    pause(.5)
    show kelvin on phone
    pause(.25)
    kel "{size=-8}...dammit, my rank dropped again.{/size}"
    mc "Rank?"
    mc "{i}What is he talking about? {/i}"
    show kelvin abashed
    pause(.25)
    kel "Oh, sorry. It's nothing; don't mind me."
    mc "{i} Looking at it more closely, the site he's on looks pretty familiar...{/i}"
    with hpunch
    mc "WAIT, YOU'RE GRANDMASTER?!?" 
    kel "Whoa? You know Leeg of Legions?!?"    
    mc "I've been playing for..."

    scene bg classroom whiteboard
    pause(.5)
    show teacher angry
    pause(.25)
    "Teacher" "Kelvin and [mc], you're being too loud!"
    "Teacher" "Why don't you two step out into the hallway?"

    scene bg hallway
    pause(.5)
    show kelvin embarrassed
    pause(.25)
    kel "Ahh, sorry to do this to you on your first day here; I was just excited to see that someone here actually plays LL."
    mc "Don't worry about it; it was my fault, too."
    mc "Also, what do you mean? Isn't LL a super popular game?"
    show kelvin neutral
    pause(.25)
    kel "It is, but most people here aren't interested in games. Everyone is too absorbed with studying or sports."
    mc "I see... Anyways, I'm only Diamond, and I've been playing for a long time."
    show kelvin happy
    pause(.25)
    kel "Still, diamond is pretty impressive!"
    "The two continue to discuss the game until the bell rings."

    show teacher neutral
    pause(.25)
    "Teacher" "Boys, you can come back in now. Next time, please try not to disrupt the lesson."
    "Kelvin and [mc]" "Sorry, it won't happen again."
    show teacher happy
    pause(.25)
    "Teacher" "Good to hear."

    scene bg classroom whiteboard
    pause(.5)
    "The rest of the classes pass by in a blur, and students are exiting the classroom."
    show kelvin happy
    pause(.25)
    kel "Hey [mc]! Hope your first day was alright."
    kel "Oh, I forgot to mention - every student needs to join a club."
    kel "Are there any clubs that you have in mind?"
    mc "Not really...now that I think about it, there was somebody trying to get me to join their club pretty desperately."
    show kelvin neutral
    pause(.25)
    kel "Oh, that's probably the e-Gaming club. They need one more member to officially register as a club but the deadline is coming up soon."
    mc "That sounds like a club I'd be interested in."
    kel "Well, they don't really play any competitive games."
    kel "It's basically a social club rather than a game-focused club."
    mc "Oh..."
    kel "I'm assuming you're not interested? Oh well, there are tons of established clubs here."
    kel "For example, I'm in the tennis club."
    show kelvin handing paper
    pause(.25)
    kel "Here's a full list of clubs if you want to take a look."
    hide kelvin handing paper
    pause(.25)
    mc "Hmm..."
    mc "I don't see any clubs that really interest me."
    show kelvin neutral
    pause(.25)
    kel "That's too bad..."
    hide kelvin neutral
    pause(.25)
    mc "{i}My only hobby is LL I guess...{/i}"
    mc "{i}It's a shame that the students here don't seem to know much about the game.{/i}"
    with hpunch
    mc "{size=+10}{i}!!!{/i}{/size}"
    mc "Hey Kelvin, about that club deadline. When is it?"
    show kelvin thinking
    pause(.25)
    kel "Hm? I think is was by the end of the week. Today is Thursday so that means..."
    mc "{i} With only one day it'll be difficult to find other people...{/i}"
    kel "Why? Got an idea for something?"
    mc "Yeah, maybe. Could I get your help with it?"
    show kelvin smile #could be same thing as kelvin happy
    pause(.25)
    kel "Of course, what is it?"
    mc "After talking with you, I realized that it felt good to share my love of LL with someone..."
    mc "So - um -"
    mc "I was thinking that we could start a LL club."
    kel "Count me in!"
    show kelvin uncertain #maybe kelvin thinking
    pause(.25)
    kel "But with only one day..."
    mc "I know it'll be hard, but I believe we can do it."
    mc "We'll find our members tomorrow."
    show kelvin smile
    pause(.25)
    kel "Okay, let's do it."
    hide kelvin smile
    pause(.25)
    "The bell rings." #add sound maybe?
    show kelvin neutral
    pause(.25)
    kel "Shoot, I better get going. Tennis practice is going to start soon."
    kel "I'll see you tomorrow [mc]."
    mc "See you tomorrow."

    scene bg neighborhood street
    with fade
    pause(1)
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
    pause(.5)
    window show
    show kelvin smile
    pause(.25)
    kel "Hey. You ready?"
    mc "Sure."
    kel "We're going to make it happen. You believe, right?"
    mc "Yeah..."
    kel "C'mon, let's go."
    mc "{i}Okay, calm down. You can do this...{/i}"

    scene bg classroom desk
    pause(.5)
    mc "{i}Alright, I'll ask the first person I see. {/i}"
    "..."
    show regina back
    pause(.25)
    mc "{i}Ok, Ok - Let's go over it one more time.{/i}"
    mc "{i}...{/i}"
    mc "{i}\"Hi, I'm [mc].\"{/i}"
    mc "{i}\"Would you like to join my club?\"{/i}"
    mc "{i}\"What is it? Oh, it's a LL club. LL is a game about...\"{/i}"
    show regina angry
    pause(.25)
    "Random Girl" "Hey! Were you staring at me?"
    mc "No! Of course not! I mean.."
    mc "I didn't mean to! - ehr - I was thinking to myself..."
    show regina neutral
    pause(.25)
    "Random Girl" "Hmph, okay."
    "Random Girl" "What were you thinking about?"
    mc "Nothing! Well, I mean, um, actually-"
    show regina smile
    pause(.25)
    "Random Girl" "It's ok, you don't have to tell me."
    "Random Girl" "Are you sure there wasn't something you wanted to say to me?"
    mc "Yea, I guess not..."
    "Random Girl" "I'll see you, then."
    mc "Bye..."
    mc "{i}Shoot! I messed up.{/i}"
    mc "{i}But it wasn't that bad, right?{/i}"

    scene bg classroom whiteboard
    pause(.5)
    "Teacher" "Alright, get your textbooks out."
    mc "{i}I guess I'll have to wait until lunch for my next shot.{/i}"

    scene bg black screen
    "..."

    scene bg cafeteria
    pause(.5)
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
    pause(.5)
    show dylan neutral
    pause(.25)
    mc "Hi ... I'm [mc]-"
    "???" "Oh hey, I'm Dylan"
    show dylan happy
    pause(.25)
    d "Wait, I know you!"
    d "Are you perhaps here..." 
    extend "to talk about the e-Gaming club?!?"  with vpunch    #i dont think we have dylan pog
    mc "Uh, about that ..."
    show dylan sad #dejected just change name of file doesn't really matter
    pause(.25)
    d "Oh..."
    mc "Sorry, I actually wanted to talk to you about a club I'm starting."
    mc "I need members for a competitive LL club."
    mc "You're in the e-Gaming club, right?"
    mc "So I was wondering if you knew anyone who would be interested..."
    show dylan thinking
    pause(.25)
    d "Hmm... Not really, sorry."
    d "In fact, we barely found our last member for the e-Gaming club."
    show dylan smile # or happy idk
    pause(.25)
    d "Good luck finding your members, though."
    mc "That's too bad..."
    mc "Thanks anyways! I'll see you around, Dylan."
    d "Bye [mc]."

    scene bg classroom desk
    pause(.5)
    mc "{i}I asked a couple more people, but nobody was really interested...{/i}"
    mc "{i}Approaching people is a lot harder than I thought.{/i}"
    mc "{i}But I think I'm making progress!{/i}"
    mc "{i}I can talk to Dylan and Kelvin without sounding completely incoherent.{/i}"
    show kelvin happy
    pause(.25)
    kel "Hey, did you manage to find anyone that was willing to join?"
    mc "Ah..."
    mc "I didn't manage to find anyone interested in joining..."
    mc "Sorry about that, even after asking for your help with something like this..."
    kel "Oh, don't worry about it! I already got 4 members!"
    with hpunch
    mc "{size=+10}WHAT??!?!{/size}" 
    mc "THANK YOU, KELVIN! YOU'RE SERIOUSLY THE BEST!"
    show kelvin smile scratching head
    pause(.25)
    kel "Haha, no worries! I have many connections with people around here~"
    kel "I'll introduce everyone to you tomorrow!"
    show kelvin happy
    pause(.25)
    kel "Also, I've already submitted a club registration to the principal."
    kel "We'll be using room F-143."
    mc "{i}Kelvin's pretty incredible...{/i}"
    mc "{i}I found it pretty hard to even approach people, but he's already gone and found enough people for me.{/i}"
    mc "{i}Without him, I don't know what I would have done...{/i}"
    kel "If you need to reach me, here's my number."
    mc "Oh thanks, here's mine as well."
    mc "{i}No way I'm telling him my mom and sister are the only ones on my contacts list.{/i}"
    show kelvin smile
    pause(.25)
    kel "Anyways, I need to get going to tennis practice now."
    kel "See you at the meeting, [mc]."
    mc "Bye, Kelvin."

    scene bg neighborhood street
    pause(1)
    mc "{i}I can't believe that Kelvin actually managed to recruit enough members for our club.{/i}"
    mc "{i}I wonder what everyone will be like...{/i}"

    scene day three
    window hide
    with Fade(.5, 1, .5)
    pause

    scene club room
    with fade
    pause(1)
    window show
    mc "{i}So this is the clubroom.{/i}"
    show kelvin neutral
    pause(.25)
    kel "Oh, [mc], you're already here."
    kel "Sorry to have kept you waiting."
    kel "Well, let me introduce you to everyone."
    hide kelvin neutral
    show tiffany shy at left
    show maryanne neutral at centerleft
    show regina power stance at centerright
    show kristella happy at right #could be kristella smile (no clue yet)
    pause(.25)
    "..."
    with hpunch
    mc "{i}{size=+8}WHAT? THEY'RE ALL GIRLS?!?!?{/size}{/i}"
    hide tiffany shy at left
    hide maryanne neutral at centerleft
    hide regina power stance at centerright
    hide kristella happy at right 
    pause(.5)
    show tiffany shy
    pause(.25)
    "Girl 1" "H-Hi, m-my name is T-tiffany."
    t "S-sorry, I'm just a bit nervous..."
    show maryanne smile
    pause(.25)
    "Girl 2" "Hey!"
    ma "It's me - er, I mean, I'm Maryanne."
    show regina power stance
    pause(.25)
    "Girl 3" "Hey! I'm Regina."
    show regina pout
    pause(.25)
    r "I'm only here for the club, so don't try anything."
    show kristella happy
    pause(.25)
    "Girl 4" "Heyyy~ I'm Kristella!"
    kr "I hope we get to know each other better."
    show tiffany shy at left
    show maryanne neutral at centerleft
    show regina power stance at centerright
    show kristella happy at right #could be kristella smile (no clue yet)
    pause(.25)
    mc "Nice to meet y'all."
    mc "{i}Wow. Everyone is so different...{/i}"
    hide tiffany shy at left
    hide maryanne neutral at centerleft
    hide regina power stance at centerright
    hide kristella happy at right 
    pause(.5)
    show kelvin smile
    pause(.25)
    kel "Great! Now that everyone knows one another, we can start with the meeting."
    kel "[mc], what did you have planned?"
    mc "-Me?"
    kel "It's your club after all!"
    mc "Uh... I - um - didn't really plan anything."
    mc "{i}What should we do?{/i}"
    show kristella neutral
    pause(.25)
    kr "Why don't we get to know everyone better"
    mc "Sure..."
    show kelvin neutral
    pause(.25)
    kel "Sounds good! I'll go get some snacks."
    hide kelvin neutral
    pause(.25)
    mc "{i}Who should I talk to first?{/i}"
    while girlsTalkedTo <= 3: 
    
        menu:
            "Tiffany" if whoFirst != "Tiffany" and whoSecond != "Tiffany" and whoThird != "Tiffany":
                jump tiffany 

            "Maryanne" if whoFirst != "Maryanne" and whoSecond != "Maryanne" and whoThird != "Maryanne":
                jump maryanne 

            "Regina" if whoFirst != "Regina" and whoSecond != "Regina" and whoThird != "Regina":
                jump regina 

            "Kristella" if whoFirst != "Kristella" and whoSecond != "Kristella" and whoThird != "Kristella":
                jump kristella 

        label tiffany:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Tiffany"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Tiffany"
            elif girlsTalkedTo == 3:
                $ whoThird = "Tiffany"
            show tiffany looking away
            pause(.25)
            t "..."   
            mc "..."
            t "..."
            "..."
            mc "{i}I guess I should say something{/i}"
            mc "Hey, Tiffany."
            show tiffany shy
            pause(.25)
            t "H-hey [mc]."
            mc "{i}She seems uncomfortable. What should I say?{/i}"

            menu:
                "Tiffany, you don't need to be nervous...":
                    jump tiffany_question_one_option_one

                "Is there something wrong?":
                    jump tiffany_question_one_option_two

                "Your stutter is super cute.":
                    jump tiffany_question_one_option_three

            label tiffany_question_one_option_one:
                mc "Tiffany, you don't need to be nervous..."
                show tiffany embarrassed #prob same thing as shy
                pause(.25)
                t "S-sorry... I c-can't help it."
                t "I'll try h-harder..."
                mc "Haha, don't worry about it."
                show tiffany shy smile
                pause(.25)
                t "Okay..."
                jump tiffany_question_one_ending

            label tiffany_question_one_option_two:
                mc "Is there something wrong?"
                show tiffany shy
                pause(.25)
                t "A-ah, I'm sorry... I'm still a b-bit nervous."
                mc "O-oh, am I scaring you? Sorry..."
                show tiffany shy smile
                pause(.25)
                t "It's alright"
                jump tiffany_question_one_ending

            label tiffany_question_one_option_three:
                mc "Your stutter is super cute."
                show tiffany blush
                pause(.25)
                t "W-wha...? Really?"
                mc "Yeah, seriously."
                show tiffany shy smile
                pause(.25)
                t "T-thanks..."
                jump tiffany_question_one_ending

            label tiffany_question_one_ending:
                show tiffany shy
                mc "{i}Cute smile...{/i}"

            mc "{i}Shoot, what now?{/i}"
            menu:
                "So, why did you join the club?":
                    jump tiffany_question_two_option_one

                "What's your relationship with Kelvin":
                    jump tiffany_question_two_option_two

                "What club were you in before this?":
                    jump tiffany_question_two_option_three

            label tiffany_question_two_option_one:
                mc "So, why did you join the club?"
                show tiffany embarrassed
                pause(.25)
                t "Um... I wanted to meet new people, I guess."
                mc "{i}New faces. I'm familiar with that...{/i}"
                mc "What for?"
                t "Hm... I - k-kinda wanted to -um, get out a bit more..."
                mc "That's great, Tiffany."
                mc "{i}Maybe I should learn from her...{/i}"
                show tiffany shy smile
                pause(.25)
                t "Y-you think so, [mc]? Thanks..."
                jump tiffany_question_two_ending

            label tiffany_question_two_option_two:
                mc "What's your relationship with Kelvin?"
                show tiffany smile
                pause(.25)
                t "Oh! We knew each other as children but never really talked until high school."
                mc "{i}How does Kelvin have so many connections?{/i}"
                mc "Oh, that's nice. Are you two... close?"
                show tiffany panic
                pause(.25)
                t "N-no! Of course n-n-... Oh. I m-mean, not in that way."
                show tiffany shy smile
                pause(.25)
                t "I g-guess you could say that we're good friends."
                mc "{i}D-does she like Kelvin??{/i}"
                mc "{i}She was probably just embarrassed, right{/i}"
                mc "Oh. That's nice..."
                jump tiffany_question_two_ending

            label tiffany_question_two_option_three:
                mc "What club were you in before this?"
                show tiffany shy #or looking away
                pause(.25)
                t "{size=-3}I was planning on joining the debate club.{/size}"
                mc "The deabte club!? Are you a good public speaker?"
                t "N-no, but I wanted to become more c-confident..."
                mc "Ah. Then why didn't you do it?"
                show tiffany embarrassed
                pause(.25)
                t "Well, I k-kinda chickened out..."
                t "B-besides, Kelvin asked me to j-join this one."
                mc "I see. Well, I'm glad you did!"
                mc "It's nice to have you here."
                t "..."
                mc "{i}Oh no, was that too much?{/i}"
                show tiffany shy smile
                pause(.25)
                t "T-thanks... I'm g-glad I did, too."
                jump tiffany_question_two_ending

            label tiffany_question_two_ending:
                mc "{i}A little shy but nice...{/i}"
                jump end_of_talking

        label maryanne:

        label regina:

        label kristella:

        label end_of_talking:
            if girlsTalkedTo == 4:
                mc "{i}That should be everyone...{/i}"
            else:
                mc "{i}Who should I talk to next?{/i}"

    mc "{i}Just in time, too.{/i}"            
            
        

         




    # This ends the game.

    return
