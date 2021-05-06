label chapterOneDay1to4:
    $ whoFirst = ""
    $ whoSecond = ""
    $ whoThird  = ""
    $ girlsTalkedTo = 0
    window hide
    scene bg black screen
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
        show dylan thinking
        pause(.25)
        "???" "Really? I haven't seen you around here before."
        "???" "Wait, you're a new student, aren't you?"
        show dylan handing flier
        pause(.25)
        "???" "You should join the e-Gaming club!"
        jump club_end

    label club_option_two:
        mc "No, why?"
        show dylan happy
        pause(.25)
        "???" "Great!"
        show dylan handing flier
        pause(.25)
        "???" "Please consider joining our club."
        jump club_end

    label club_option_three:
        show dylan flier angry #slight problem, we don't have an image for this
        pause(.25)
        "???" "HEY!!! I KNOW YOU HEAR ME!!!"
        scene bg school hallway
        pause(.25)
        "You continue looking forward and scurry away."
        "???" "COME TO THE E-GAMING CLUB!!!"
        jump club_end

    label club_end:
        scene bg classroom #facing whiteboard
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
    "Teacher" "[mc], why don't you take a seat next to Ethan."

    scene bg classroom #facing desks
    pause(.5)
    show ethan happy
    pause(.25)
    e "Hi, I'm Ethan. Nice to meet you, [mc]!"
    mc "Hello."
    e "If you ever need help, don't be afraid to ask."
    mc "Okay..."

    scene bg classroom
    pause(.5)
    "Teacher" "We'll be continuing from our last lesson on combinations and permutations."
    "The teacher turns around and begins writing numbers on the whiteboard behind him." #gender not known yet
    "The lesson is long-winded, and the teacher's voice is mundane."

    scene bg classroom
    with fade
    pause(.5)
    show ethan grimace #or neutral
    pause(.25)
    e "{size=-8}...dammit, my rank dropped again.{/size}"
    mc "Rank?"
    mc "{i}What is he talking about? {/i}"
    show ethan slight smile
    pause(.25)
    e "Oh, sorry. It's nothing; don't mind me."
    mc "{i} Looking at it more closely, the site he's on looks pretty familiar...{/i}"
    with hpunch
    mc "WAIT, YOU'RE GRANDMASTER?!?" 
    e "Whoa? You know Leeg of Legions?!?"    
    mc "I've been playing for..."

    scene bg classroom
    pause(.5)
    show teacher angry
    pause(.25)
    "Teacher" "Ethan and [mc], you're being too loud!"
    "Teacher" "Why don't you two step out into the hallway?"

    scene bg school hallway
    pause(.5)
    show ethan embarrassed
    pause(.25)
    e "Ahh, sorry to do this to you on your first day here; I was just excited to see that someone here actually plays LL."
    mc "Don't worry about it; it was my fault, too."
    mc "Also, what do you mean? Isn't LL a super popular game?"
    show ethan neutral
    pause(.25)
    e "It is, but most people here aren't interested in games. Everyone is too absorbed with studying or sports."
    mc "I see... Anyways, I'm only Diamond, and I've been playing for a long time."
    show ethan happy
    pause(.25)
    e "Still, diamond is pretty impressive!"
    scene bg school hallway
    "The two continue to discuss the game until the bell rings."

    show teacher neutral
    pause(.25)
    "Teacher" "Boys, you can come back in now. Next time, please try not to disrupt the lesson."
    "Ethan and [mc]" "Sorry, it won't happen again."
    show teacher happy
    pause(.25)
    "Teacher" "Good to hear."

    scene bg classroom 
    pause(.5)
    "The rest of the classes pass by in a blur, and students are exiting the classroom."
    show ethan happy
    pause(.25)
    e "Hey [mc]! Hope your first day was alright."
    e "Oh, I forgot to mention - every student needs to join a club."
    e "Are there any clubs that you have in mind?"
    mc "Not really...now that I think about it, there was somebody trying to get me to join their club pretty desperately."
    show ethan neutral
    pause(.25)
    e "Oh, that's probably the e-Gaming club. They need one more member to officially register as a club but the deadline is coming up soon."
    mc "That sounds like a club I'd be interested in."
    e "Well, they don't really play any competitive games."
    e "It's basically a social club rather than a game-focused club."
    mc "Oh..."
    e "I'm assuming you're not interested? Oh well, there are tons of established clubs here."
    e "For example, I'm in the tennis club."
    show ethan happy
    pause(.25)
    e "Here's a full list of clubs if you want to take a look."
    hide ethan happy
    pause(.25)
    mc "Hmm..."
    mc "I don't see any clubs that really interest me."
    show ethan neutral
    pause(.25)
    e "That's too bad..."
    hide ethan neutral
    pause(.25)
    mc "{i}My only hobby is LL I guess...{/i}"
    mc "{i}It's a shame that the students here don't seem to know much about the game.{/i}"
    with hpunch
    mc "{size=+10}{i}!!!{/i}{/size}"
    mc "Hey Ethan, about that club deadline. When is it?"
    show ethan thinking
    pause(.25)
    e "Hm? I think is was by the end of the week. Today is Thursday so that means..."
    mc "{i} With only one day it'll be difficult to find other people...{/i}"
    e "Why? Got an idea for something?"
    mc "Yeah, maybe. Could I get your help with it?"
    show ethan happy #could be same thing as ethan happy
    pause(.25)
    e "Of course, what is it?"
    mc "After talking with you, I realized that it felt good to share my love of LL with someone..."
    mc "So - um -"
    mc "I was thinking that we could start a LL club."
    e "Count me in!"
    show ethan thinking #maybe ethan thinking
    pause(.25)
    e "But with only one day..."
    mc "I know it'll be hard, but I believe we can do it."
    mc "We'll find our members tomorrow."
    show ethan happy
    pause(.25)
    e "Okay, let's do it."
    hide ethan happy
    pause(.25)
    "The bell rings." #add sound maybe?
    show ethan neutral
    pause(.25)
    e "Shoot, I better get going. Tennis practice is going to start soon."
    e "I'll see you tomorrow [mc]."
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
    show ethan happy
    pause(.25)
    e "Hey. You ready?"
    mc "Sure."
    e "We're going to make it happen. You believe, right?"
    mc "Yeah..."
    e "C'mon, let's go."
    mc "{i}Okay, calm down. You can do this...{/i}"

    scene bg classroom
    pause(.5)
    mc "{i}Alright, I'll ask the first person I see. {/i}"
    "..."
    show mic neutral
    pause(.25)
    mc "{i}Ok, Ok - Let's go over it one more time.{/i}"
    mc "{i}...{/i}"
    mc "{i}\"Hi, I'm [mc].\"{/i}"
    mc "{i}\"Would you like to join my club?\"{/i}"
    mc "{i}\"What is it? Oh, it's a LL club. LL is a game about...\"{/i}"
    show mic angry
    pause(.25)
    "Random Guy" "Hey! Were you staring at me?"
    mc "No! Of course not! I mean.."
    mc "I didn't mean to! - ehr - I was thinking to myself..."
    show mic neutral
    pause(.25)
    "Random Guy" "Hmph, okay."
    "Random Guy" "What were you thinking about?"
    mc "Nothing! Well, I mean, um, actually-"
    show mic smile
    pause(.25)
    "Random Guy" "It's ok, you don't have to tell me."
    "Random Guy" "Are you sure there wasn't something you wanted to say to me?"
    mc "Yea, I guess not..."
    "Random Guy" "I'll see you, then."
    mc "Bye..."
    scene bg classroom
    mc "{i}Shoot! I messed up.{/i}"
    mc "{i}But it wasn't that bad, right?{/i}"

    scene bg classroom
    with fade
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
    scene bg cafeteria two
    show random person one
    pause
    scene bg cafeteria three
    show random person two
    pause
    scene bg cafeteria four
    show dylan neutral
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
    show dylan elated
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
    show dylan happy # or happy idk
    pause(.25)
    d "Good luck finding your members, though."
    mc "That's too bad..."
    mc "Thanks anyways! I'll see you around, Dylan."
    d "Bye [mc]."

    scene bg classroom
    pause(.5)
    mc "{i}I asked a couple more people, but nobody was really interested...{/i}"
    mc "{i}Approaching people is a lot harder than I thought.{/i}"
    mc "{i}But I think I'm making progress!{/i}"
    mc "{i}I can talk to Dylan and Ethan without sounding completely incoherent.{/i}"
    show ethan happy
    pause(.25)
    e "Hey, did you manage to find anyone that was willing to join?"
    mc "Ah..."
    mc "I didn't manage to find anyone interested in joining..."
    mc "Sorry about that, even after asking for your help with something like this..."
    e "Oh, don't worry about it! I already got 4 members!"
    with hpunch
    mc "{size=+10}WHAT??!?!{/size}" 
    mc "THANK YOU, ETHAN! YOU'RE SERIOUSLY THE BEST!"
    show ethan slight smile
    pause(.25)
    e "Haha, no worries! I have many connections with people around here~"
    e "I'll introduce everyone to you tomorrow!"
    show ethan happy
    pause(.25)
    e "Also, I've already submitted a club registration to the principal."
    e "We'll be using room F-143."
    mc "{i}Ethan's pretty incredible...{/i}"
    mc "{i}I found it pretty hard to even approach people, but he's already gone and found enough people for me.{/i}"
    mc "{i}Without him, I don't know what I would have done...{/i}"
    e "If you need to reach me, here's my number."
    mc "Oh thanks, here's mine as well."
    mc "{i}No way I'm telling him my mom and sister are the only ones on my contacts list.{/i}"
    show ethan happy
    pause(.25)
    e "Anyways, I need to get going to tennis practice now."
    e "See you at the meeting, [mc]."
    mc "Bye, Ethan."

    scene bg neighborhood street
    pause(1)
    mc "{i}I can't believe that Ethan actually managed to recruit enough members for our club.{/i}"
    mc "{i}I wonder what everyone will be like...{/i}"

    scene day three
    window hide
    with Fade(.5, 1, .5)
    pause

    scene bg clubroom
    with fade
    pause(1)
    window show
    mc "{i}So this is the clubroom.{/i}"
    show ethan neutral
    pause(.25)
    e "Oh, [mc], you're already here."
    e "Sorry to have kept you waiting."
    e "Well, let me introduce you to everyone."
    hide ethan neutral
    show tiffany shy small at left
    show maryanne neutral at centerleft
    show regina power stance at centerright
    show kristella happy at right #could be kristella smile (no clue yet)
    pause(.25)
    "..."
    with hpunch
    mc "{i}{size=+8}WHAT? THEY'RE ALL GIRLS?!?!?{/size}{/i}"
    hide tiffany shy small at left
    hide maryanne neutral at centerleft
    hide regina power stance at centerright
    hide kristella happy at right 
    pause(.5)
    show tiffany shy
    pause(.25)
    "Girl 1" "H-Hi, m-my name is T-tiffany."
    t "S-sorry, I'm just a bit nervous..."
    hide tiffany shy
    show maryanne smile
    pause(.25)
    "Girl 2" "Hey!"
    ma "It's me - er, I mean, I'm Maryanne."
    hide maryanne shy
    show regina power stance
    pause(.25)
    "Girl 3" "Hey! I'm Regina."
    show regina pout
    pause(.25)
    r "I'm only here for the club, so don't try anything."
    hide regina pout
    show kristella happy
    pause(.25)
    "Girl 4" "Heyyy~ I'm Kristella!"
    kr "I hope we get to know each other better."
    hide kristella happy
    show tiffany shy small at left
    show maryanne neutral at centerleft
    show regina power stance at centerright
    show kristella happy at right #could be kristella smile (no clue yet)
    pause(.25)
    mc "Nice to meet y'all."
    mc "{i}Wow. Everyone is so different...{/i}"
    hide tiffany shy small at left
    hide maryanne neutral at centerleft
    hide regina power stance at centerright
    hide kristella happy at right 
    pause(.5)
    show ethan happy
    pause(.25)
    e "Great! Now that everyone knows one another, we can start with the meeting."
    e "[mc], what did you have planned?"
    mc "-Me?"
    e "It's your club after all!"
    mc "Uh... I - um - didn't really plan anything."
    mc "{i}What should we do?{/i}"
    hide ethan happy
    show kristella neutral
    pause(.25)
    kr "Why don't we get to know everyone better?"
    mc "Sure..."
    hide kristella neutral
    show ethan neutral
    pause(.25)
    e "Sounds good! I'll go get some snacks."
    hide ethan neutral
    pause(.25)
    mc "{i}Who should I talk to first?{/i}"
    while girlsTalkedTo <= 3: 
        scene bg clubroom
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
            show tiffany shy
            pause(.25)
            t "..."   
            mc "..."
            t "..."
            "..."
            mc "{i}I guess I should say something{/i}"
            mc "Hey, Tiffany."
            show tiffany looking away
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
                show tiffany shy #prob same thing as shy
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
                show tiffany uwu
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

                "What's your relationship with Ethan?":
                    jump tiffany_question_two_option_two

                "What club were you in before this?":
                    jump tiffany_question_two_option_three

            label tiffany_question_two_option_one:
                mc "So, why did you join the club?"
                show tiffany looking away
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
                mc "What's your relationship with Ethan?"
                show tiffany smile
                pause(.25)
                t "Oh! We knew each other as children but never really talked until high school."
                mc "{i}How does Ethan have so many connections?{/i}"
                mc "Oh, that's nice. Are you two... close?"
                show tiffany uwu
                pause(.25)
                t "N-no! Of course n-n-... Oh. I m-mean, not in that way."
                show tiffany shy smile
                pause(.25)
                t "I g-guess you could say that we're good friends."
                mc "{i}D-does she like Ethan??{/i}"
                mc "{i}She was probably just embarrassed, right{/i}"
                mc "Oh. That's nice..."
                jump tiffany_question_two_ending

            label tiffany_question_two_option_three:
                mc "What club were you in before this?"
                show tiffany shy #or looking away
                pause(.25)
                t "{size=-3}I was planning on joining the debate club.{/size}"
                mc "The debate club!? Are you a good public speaker?"
                t "N-no, but I wanted to become more c-confident..."
                mc "Ah. Then why didn't you do it?"
                show tiffany looking away
                pause(.25)
                t "Well, I k-kinda chickened out..."
                t "B-besides, Ethan asked me to j-join this one."
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
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Maryanne"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Maryanne"
            elif girlsTalkedTo == 3:
                $ whoThird = "Maryanne"
            show maryanne patty eyes #idk wtf this is
            pause(.25)
            ma "Hey [mc]... It's been a while."
            mc "Huh? What are you talking about?"
            show maryanne shocked
            pause(.25)
            ma "{cps=*3}{size=-8}{i}Oh ... d-does he not remember me?{/i}{/size}{/cps}"
            mc "Sorry, what was that? I couldn't hear you."
            show maryanne embarrassed smile
            ma "Oh nothing! I was just thinking out loud."
            mc "Oh, I see. Anyways..."
            menu:
                "What do you think about games?":
                    jump maryanne_question_option_one

                "How did you meet Ethan?":
                    jump maryanne_question_option_two

                "Why did you decide to join this club?":
                    jump maryanne_question_option_three

            label maryanne_question_option_one:
                mc "What do you think about games?"
                show maryanne giggle
                pause(.25)
                ma "Well, I like games of course! I wouldn't be here if I didn't right, silly?"
                mc "U-uh, I guess so..."
                show maryanne slight smile #head tilted
                pause(.25)
                ma "What about you? How did you get into games?"
                mc "Hmm...actually, I've pretty much always enjoyed games. I vividly remember the first time I used a computer."
                mc "I was probably four or five, and I've been in love ever since."
                show maryanne aggressive glare
                pause(.25)
                ma "Oh...me too. I feel like we always remember the important parts of our childhood, don't you?"
                mc "Oh yeah, for sure. I thi- wait, why d-do you look so angry?"
                show maryanne fake smile
                pause(.25)
                ma "Oh, it's nothing. Don't worry about it."
                mc "Oh, alright. If you say so."
                show maryanne aggressive glare
                pause(.25)
                ma "..."
                mc "{i}I should probably go...{/i}"
                mc "Well, see you later, Maryanne..."
                ma "..."
                mc "{i}What did I do?!?{/i}"
                jump maryanne_question_end

            label maryanne_question_option_two:
                mc "How did you meet Ethan?"
                show maryanne smile
                pause(.25)
                ma "Well, we were both in the competitive math club our freshman year. He's a good friend, isn't he?"
                mc "Yeah, he really is! I just met him, but I feel like we've known each other forever..."
                show maryanne excited #idk about frothing at the mouth my dude
                pause(.25)
                ma "It sure feels like we have!" with vpunch
                mc "W-wha? What are you talking about??"
                show maryanne embarrassed smile
                pause(.25)
                ma "Oh, sorry... I just meant that I've known Ethan for a long time. We're pretty close..."
                mc "I knew it!"
                show maryanne blushing #and laughing as well i guess?
                pause(.25)
                ma "No, not in that way! I already like somebody else..."
                mc "Hehe, I was just kidding."
                show maryanne pout
                pause(.25)
                ma "Not funny."
                mc "Heh, alright, I'll see you later, Maryanne."
                show maryanne smile
                pause(.25)
                ma "Bye, [mc]."
                mc "{i}I wonder who she's into...{/i}"
                jump maryanne_question_end

            label maryanne_question_option_three:
                mc "Why did you decide to join this club?"
                show maryanne neutral
                pause(.25)
                ma "Well, the club I was planning on joining disbanded due to leadership issues."
                mc "Ah, that's unfortunate, but I hope you'll enjoy this club."
                show maryanne smile
                pause(.25)
                ma "Of course I will, {cps=*3}{size=-8}{i}you're in it...{/i}{/size}{/cps}"
                mc "What did you say?"
                show maryanne shy smile
                pause(.25)
                ma "Oh, I was just thinking out loud."
                mc "{i}I guess she just has a habit of thinking out loud.{/i}"
                mc "Okay, I'll see you later."
                ma "Later, [mc]."
                jump maryanne_question_end
            
            label maryanne_question_end:
                jump end_of_talking      

        label regina:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Regina"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Regina"
            elif girlsTalkedTo == 3:
                $ whoThird = "Regina"
            show regina arms crossed #or powerstance idk
            pause(.25)
            mc "..."
            r "Hey, why are you looking at me like that?"
            mc "Uh, I was trying to think of something to say."
            r "Then spit it out. I don't have all day for this."
            mc "{i}Why is she so aggressive towards me? How do I start a conversation with her?{/i}"
            menu:
                "What'd you even come here for?":
                    jump regina_question_one_option_one

                "Are you always this rude?":
                    jump regina_question_one_option_two

                "What did I do to anger you?":
                    jump regina_question_one_option_three

            label regina_question_one_option_one:
                mc "What'd you even come here for?"
                show regina angry
                pause(.25)
                r "Wow. What's that supposed to mean?"
                mc "{i}... I may have made a mistake.{/i}"
                r "I'm here becuae I want to be, duh. Any more stupid questions?"
                mc "N-no..."
                jump regina_question_one_end

            label regina_question_one_option_two:
                mc "Are you always this rude?"
                show regina stern
                pause(.25)
                r "I'm always like this."
                r "What, did you think you were special?"
                mc "I mean, of course not, that's not wh-"
                r "Good, because you're not."
                mc "... Understood."
                jump regina_question_one_end

            label regina_question_one_option_three:
                mc "What did I do to anger you?"
                r "Hmph, this is how I normally talk to people."
                mc "I see... But can you be a little nic-"
                r "No."
                mc "..."
                jump regina_question_one_end

            label regina_question_one_end:
                mc "Anyways..."
            
            menu:
                "How do you know Ethan?":
                    jump regina_question_two_option_one

                "Do you enjoy playing games?":
                    jump regina_question_two_option_two

                "Um... how well do you get along with others?":
                    jump regina_question_two_option_three

            label regina_question_two_option_one:
                mc "How do you know Ethan?"
                r "Oh that guy, I had a class with him last year and we sat next to each other."
                mc "{i}How did Ethan put up with this girl for a year? He's amazing as usual.{/i}"
                mc "I see... What was he like?"
                show regina arms crossed looking away
                pause(.25)
                r "Hmph, aren't you in one of his classes? You can expreience him for yourself."
                mc "Understood..."
                mc "{i}She's kinda scary...{/i}"
                jump regina_question_two_end

            label regina_question_two_option_two:
                mc "Do you enjoy playing games?"
                show regina glare
                pause(.25)
                r "Of course I do. If I didn't, why would I be here? You're dense."
                mc "Err s-sorry... this was just a genuine question."
                r "Hmph. Games allow me to relax and take my mind off of bigger issues."
                mc "I can understand that. Everyone goe-"
                show regina angry
                pause(.25)
                r "Did I ask? I don't need your help."
                mc "N-no, o-of course n-not..."
                mc "{i}Geez{/i}"
                jump regina_question_two_end

            label regina_question_two_option_three:
                mc "Um... how well do you get along with others?"
                show regina angry
                pause(.25)
                r "What are you trying to imply?"
                r "I don't have any problems with other people."
                r "It's not my fault that you're a big baby."
                mc "..."
                mc "Please don't hurt me..."
                show regina evil smile
                pause(.25)
                r "Don't annoy me any more, and I'll consider it."
                mc "{i}I better take this opportunity to get out...{/i}"
                jump regina_question_two_end

            label regina_question_two_end:
                jump end_of_talking

        label kristella:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Kristella"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Kristella"
            elif girlsTalkedTo == 3:
                $ whoThird = "Kristella"
            show kristella smile
            pause(.25)
            kr "Hey, [mc]! How's everything going?"
            mc "Hi, Kristella..."
            show kristella concerned
            pause(.25)
            kr "Hey, you look uncomfortable. What's wrong, [mc]?"
            menu:
                "Nothing":
                    jump kristella_question_one_option_one

                "I ate something weird":
                    jump kristella_question_one_option_two

                "You":
                    jump kristella_question_one_option_three

            label kristella_question_one_option_one:
                mc "Oh, wha-uhm, ehr... it's nothing!!"
                kr "Hmm... Are you sure?"
                kr "If you tell me what's wrong, I can help you out~"
                mc "No! I'm fine! There's nothing wrong!"
                show kristella laughing
                pause(.25)
                kr "Okay, fine. I'll trust you, hehe."
                mc "Good"
                mc "{i}Phew. That was stressful.{/i}"
                jump kristella_question_one_end

            label kristella_question_one_option_two:
                mc "Uh, I think I ate something weird..."
                kr "Oh no! Are you alright?"
                mc "Yeah, don't worry about me."
                kr "I'm not convinced..."
                show kristella lightbulb #have an idea, idk 
                pause(.25)
                kr "Hold on, I can help!"
                show kristella stern
                pause(.25)
                kr "Lie down, and don't move."
                mc "Okay, fine."
                scene bg clubroom
                with fade
                pause(.5)
                "Five minutes later, Kristella scurries back into the room."
                show kristella panting
                pause(.25)
                kr "{cps=30}Haa... hold on, let me catch my breath.{/cps}"
                kr "..."
                show kristella handing pepto
                pause(.25)
                kr "Here, take this. I got it from the nurse."
                show kristella smile
                pause(.25)
                kr "It should make you feel better..."
                mc "..."
                mc "{i}It might be placebo, but I already feel better...{/i}"
                mc "Wow, Kristella. Thank you so much."
                show kristella giggle
                pause(.25)
                kr "Don't mention it, MC~"
                jump kristella_question_one_end

            label kristella_question_one_option_three:
                mc "It's you..."
                kr "Oh, sorry... I know I can be a bit much at ti-"
                mc "No, no! That's not what I meant."
                mc "I'm just- um- not used to this..."
                show kristella confused
                pause(.25)
                kr "Huh? What do you mean?"
                mc "Ah... you know, erm, talking to um... popu-"
                show kristella smile
                pause(.25)
                kr "[mc], don't worry about that!"
                kr "Let's act like old friends~"
                mc "{i}That sounds a bit strange...{/i}"
                mc "Um, okay..."
                jump kristella_question_one_end
            
            label kristella_question_one_end:
                mc "{i}Okay, what should I say...{/i}"

            menu:
                "Why did you decide to join this club?":
                    jump kristella_question_two_option_one

                "Ethan's lucky to know you...":
                    jump kristella_question_two_option_two   

            label kristella_question_two_option_one:
                mc "Why did you decide to join this club?"
                show kristella laughing
                pause(.25)             
                kr "Well... I don't really know~"
                kr "It was kind of an impulsive decision."
                kr "But I'm glad I did. I think we'll have lots of fun!"
                mc "Um... er, yeah, I h-hope so..."
                mc "I'm uh- glad you're here."
                show kristella giggle
                pause(.25)
                kr "Thanks~ I'm glad you're here as well."
                jump kristella_question_two_end

            label kristella_question_two_option_two:
                mc "Ethan's lucky to know you..."
                show kristella smile
                pause(.25)
                kr "Oh, I think you misunderstand."
                kr "I met Ethan for the first time yesterday."
                mc "{i}K-Ethan randomly approached her?{/i}"
                mc "Wow... how did Ethan convince you to join the club?"
                kr "Actually, I noticed him in the hallway with his head down."
                kr "He looked dismayed, so I asked him what happened, and he told me that he needed members for a club."
                kr "I wanted to help, so here I am."
                mc "That's very nice of you. Thank you."
                show kristella laughing
                pause(.25)
                kr "Hehe~ No problem."
                jump kristella_question_two_end

            label kristella_question_two_end:
                jump end_of_talking

        label end_of_talking:
            if girlsTalkedTo == 4:
                scene bg clubroom
                mc "{i}That should be everyone...{/i}"
            else:
                scene bg clubroom
                mc "{i}Who should I talk to next?{/i}"

    mc "{i}Just in time, too.{/i}" 
    mc "Um... L-listen up, everyone..."    
    pause(.5) 
    mc "That's all the time we have for today, so I'll see y'all tomorrow."
    mc "Thank you for coming."
    show ethan neutral
    pause(.25)
    e "Later [mc]."
    hide ethan neutral
    pause(.5)
    show tiffany looking away
    pause(.25)
    t "T-thank you, [mc]."
    hide tiffany looking away
    pause(.5)
    show maryanne slight smile
    pause(.25)
    ma "Goodbye, [mc]."
    hide maryanne slight smile
    pause(.5)
    show regina pout
    pause(.25)
    r "Hmph. Bye."
    hide regina pout
    pause(.5)
    show kristella laugh
    pause(.25)
    kr "It was fun! See you around, [mc]~"
    hide kristella laugh
    pause

    scene bg neighborhood street
    with fade
    pause(.5)
    mc "{i}Meeting everyone was pretty cool...{/i}"
    mc "{i}It went better than expected.{/i}"
    mc "{i}I'm excited for tomorrow's meeting.{/i}"
    mc "{i}Ethan and I can teach everyone about LL, and we can continue to get to know each other better...{/i}"

    scene day four
    window hide
    with Fade(.5, 1, .5)
    pause

    scene bg clubroom
    with fade
    pause(.5)
    show tiffany neutral small at left
    show maryanne neutral at centerleft
    show regina neutral at centerright
    show kristella neutral at right
    pause(.25)
    window show
    mc "Hello, everyo-"
    scene bg clubroom
    show ethan panic
    pause(.25)
    e "Bad news, guys."
    e "The principal decided that we don't qualify as an official club."
    pause(.25)
    with hpunch
    pause(.25)
    e "Apparently, we aren't different enough from the e-Gaming club."
    hide ethan panic
    show kristella concerned
    pause(.25)
    kr "Oh no!"
    hide kristella concerned
    show tiffany sad
    pause(.25)
    t "W-wow... that's not g-good."
    hide tiffany sad
    show regina annoyed
    pause(.25)
    r "Ugh. Stupid principal."
    hide regina annoyed
    show maryanne thinking
    pause(.25)
    ma "Everyone calm down. Think, what can we do?"
    hide maryanne thinking
    show ethan neutral
    pause(.25)
    e "Yeah, Maryanne's right. [mc], what do you think?"
    scene bg clubroom
    pause(.25)
    mc "{i}Well, I know I don't want to let this stop the club...{/i}"
    mc "Err... I don't know about you guys..."
    mc "But I really like this club already-"
    show kristella smile 
    pause(.25)
    kr "Yes~ we do too!"
    mc "And um- well, I don't think we should let this stop us."
    hide kristella smile
    show regina determined
    pause(.25)
    r "Hmph. You're right."
    mc "A-although I don't really have any ideas yet..."
    hide regina determined
    show tiffany shy
    pause(.25)
    t "T-that's alright [mc]."
    mc "If we all work together, I'm sure we'll figure something out."
    hide tiffany shy
    show maryanne smile
    pause(.25)
    ma "Of course we will."
    hide maryanne smile
    show ethan excited
    pause(.25)
    e "Yeah! Let's all start brainstorming. Any ideas to start us off?"
    hide ethan excited
    show regina evil smile
    pause(.25)
    r "Me!"
    mc "Okay, go ahead."
    r "If the principal doesn't want to recognize us, we will force him to!"
    r "Heres the plan:" 
    r "We storm into his office," 
    r "slam the desk," 
    r "and demand that he changes his mind!"
    r "And if that doesn't do it, then we'll have to..."
    show regina evil laugh
    pause(.25)
    r "FORCIBLY REMOVE HIM FROM HIS POSITION!!!" with hpunch
    pause(.5)
    mc "..."
    hide regina evil laugh
    show ethan annoyed #replace with better expression 
    pause(.25)
    e "Um... Thanks for the input, but I think that may be a little too troublesome."
    hide ethan annoyed
    show kristella neutral
    pause(.25)
    kr "I agree..."
    hide kristella neutral
    show regina annoyed
    pause(.25)
    r "Grr... fine. Y'all are a bunch of scaredy-cats."
    hide regina annoyed
    show ethan neutral
    pause(.25)
    e "Anyone else?"
    hide ethan neutral
    show tiffany looking away
    pause(.25)
    t "Um, I c-can't think of anything- s-sorry..."
    mc "It's alright, Tiffany. Maryanne, any ideas?"
    hide tiffany looking away
    show maryanne thinking
    pause(.25)
    ma "Hmm... first, we should establish the conditions for qualifications as an official club."
    show maryanne reading
    pause(.25)
    ma "If we analyze this clause in the student handbook, these are the requirements in simple terms:" 
    ma "1) The proposed club shall have, at minimum, five members who are not already dedicated to a separate organization." 
    ma "2) The proposed club will be centered around an activity that is school-appropriate, as defined by the jurisdiction of the principal."
    ma "3) The proposed club must have unique elements distinguishing it from pre-existing organizations, including, but not limited to, separate focus, competitive prowess, and/or new acti-"
    hide maryanne reading
    show kristella excited
    pause(.25)
    kr "That's it - competitiveness!"
    kr "We can separate ourselves from the e-Gaming club by entering and winning a competition!"
    hide kristella excited
    show tiffany aghast
    pause(.25)
    t "C-c...competition???"
    hide tiffany aghast
    show maryanne smile
    pause(.25)
    ma "Hmm.. that would satisfy the conditions for qualification."
    ma "However, we lack the experience and game knowledge necessary to place highly."
    hide maryanne smile
    show ethan neutral
    pause(.25)
    e "There's still time for you all to get familiar with the game before the tournament-"
    e "But it'll require a lot of effort."
    hide ethan neutral
    show regina smile
    pause(.25)
    r "I'm down. Let's do it!"
    hide regina smile
    show ethan neutral
    pause(.25)
    e "Unfortunately, you all will have to play without me."
    hide ethan neutral
    show tiffany aghast
    pause(.25)
    t "W-whyy??"
    hide tiffany aghast
    show ethan slight smile
    pause(.25)
    e "Between tennis tournaments and my other LL team, I won't have time to participate."
    extend "I'm sorry, but there are five of you anyways, the perfect number fo an LL team."
    mc "Yeah... Let's do it guys."
    hide ethan slight smile
    show kristella questioning
    pause(.25)
    kr "Okay, then. [mc], thoughts?"
    scene bg clubroom
    mc "Yeah... Let's do it, guys."
    show kristella smile
    pause(.25)
    kr "Yay!"
    hide kristella smile
    pause(.25)
    show tiffany shy smile
    pause(.25)
    t "O-okay..."
    hide tiffany shy smile
    pause(.25)
    show maryanne smile
    pause(.25)
    ma "Good plan."
    hide maryanne smile
    pause(.25)
    show regina smile
    pause(.25)
    r "The other teams better get ready to go down!"
    hide regina smile
    pause(.25)

    scene bg neighborhood street
    with fade
    pause(.5)
    mc "{i}Wow... I guess these are my new teammates:{/i}"
    mc "{i}Maryanne, Regina, Kristella, and Tiffany-{/i}"
    mc "{i}What type of a team will we be?{/i}"
    
    jump chapterOneDay5

    return
