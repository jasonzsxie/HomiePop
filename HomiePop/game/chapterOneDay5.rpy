﻿label chapterOneDay5:
    $ whoFirst = ""
    $ whoSecond = ""
    $ whoThird  = ""
    $ girlsTalkedTo = 0
    window hide
    scene day five
    pause

    scene bg clubroom 
    with fade
    pause(.5)
    window show
    show tiffany neutral left
    show regina neutral centerleft
    show maryanne neutral centerright  
    show kristella neutral right
    pause(.25)
    mc "Today I'll be assigning roles to all of you."
    "All Females" "Roles?"
    scene bg clubroom
    show kelvin excited
    pause(.25)
    kel "Yup! MC, would you like to explain?"
    mc "Right."
    scene league maryanne_question_option_one
    mc "LL is a team oriented strategy based game where 5 players fight each other, working their way to the other team's crystal."
    mc "The objective is to break the opponent's crystal before the other team gets to yours."
    mc "There are 3 lanes and a jungle, which contains neutral monsters that can be slain for resources or team buffs"
    mc "Each member of the team has a different role -from top, jungle, mid, adc (short for attack damage carry), and support, which involves different responsibilities."
    mc "For example, I am a Jungle main, so I'm responsible for helping all of my teammates and securing neutral objectives."
    mc "Top makes individual plays and engages teamfights."
    mc "Mid usually controls decision-making and strategy."
    mc "ADC tries to stay safe and do damage later in the game."
    mc "ADC and Support play together in the bottom lane. The Support takes care of the ADC and helps the team maintain vision of the map."
    mc "Sooo, did everyone understand that?"
    scene bg clubroom
    show tiffany confused left
    show regina confused centerleft
    show maryanne confused centerright  
    show kristella confused right
    pause(.25)
    "All Females" "Kinda...?" 
    scene bg clubroom
    show kelvin exasperated
    pause(.25)
    mc "You're probably right..."
    mc "We should get roles decided first."
    mc "{i}Who should I talk to? {i}"
    while girlsTalkedTo <= 3: 
        scene bg clubroom
        menu:
            "Tiffany" if whoFirst != "Tiffany" and whoSecond != "Tiffany" and whoThird != "Tiffany":
                jump tiffanyRole 

            "Maryanne" if whoFirst != "Maryanne" and whoSecond != "Maryanne" and whoThird != "Maryanne":
                jump maryanneRole 

            "Regina" if whoFirst != "Regina" and whoSecond != "Regina" and whoThird != "Regina":
                jump reginaRole 

            "Kristella" if whoFirst != "Kristella" and whoSecond != "Kristella" and whoThird != "Kristella":
                jump kristellaRole 

        label tiffanyRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Tiffany"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Tiffany"
            elif girlsTalkedTo == 3:
                $ whoThird = "Tiffany"
            show tiffany nervous
            pause(.25)
            mc "Hey Tiffany."
            t "H-hi."
            mc "No Need to be nervous. Justing going to ask some questions."
            menu:
                "What role sounds fun for you?":
                    jump tiffanyRoleOne
                "Did you understand the point of the game?":
                    jump tiffanyRoleTwo
                "You would be a great ADC player.":
                    jump tiffanyRoleThree

            label tiffanyRoleOne:
                show tiffany shy smile
                pause(.25)
                t "U-uh, I like the role ADC more than all the other roles"
                mc "Oh, why's that?"
                t "B-because I get to stay far away from the enmy and I'm protected."
                mc "But you'll have a lot of pressure later in the game to carry. Do you think you can handle the pressure?"
                show tiffany smile
                pause(.25)
                t "Yeah, I think I can handle the pressure"
                jump endTiffanyRole
            
            label tiffanyRoleTwo:   
                show tiffany nervous
                pause(.25)
                t "Er-r, we just try to destroy the enemy crystal right? And each person has a role to play."
                mc "{i}So she did understand...{/i}"
                mc "Yeah, that's pretty much it. So have you decided on a role?"
                show tiffany slight smile
                pause(.25)
                t "A-ADC sounds kinda fun, b-because I get to be protected and far from the enemy."
                mc "Oh, but you're going to have a large weight on you back late in the game. Are you able to withstand that pressure?"
                show tiffany smile 
                pause(.25)
                t "You can count on me."
                jump endTiffanyRole

            label tiffanyRoleThree:
                show tiffany surprised
                pause(.25)
                t "A-ADC?!?! W-why do you think I would be good at it?"
                mc "Well, you seem like you would enjoy being protected by the team. Plus, there will be someone playing with you to get you through the early stages of the game."
                show tiffany nervous
                pause(.25)
                t "D-don't I have a lot of pressure later in the game to carry?"
                mc "I believe in your ability to withstand that pressure."
                show tiffany smile
                pause(.25)
                t "Thanks. I won't let you down."
                jump endTiffanyRole

            label endTiffanyRole:
                jump endOfRole

        label maryanneRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Maryanne"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Maryanne"
            elif girlsTalkedTo == 3:
                $ whoThird = "Maryanne"
            show maryanne smile
            mc "Hi Maryanne."
            ma "Hey [mc]"
            mc "Let's get to the point."
            menu:
                "Did you understand the point of each role?":
                    jump maryanneRoleOne
                "What role do you think you would enjoy?":
                    jump maryanneRoleTwo
                "I think you should play mid.":
                    jump maryanneRoleThree
                
            label maryanneRoleOne:
                show maryanne excited
                pause(.25)
                ma "Mid sounds fun. I get to help impact all the other lanes and set the tempo of the game."
                mc "Yep, that's essentially what the Mid laner has to do."
                ma "Hmm... I feel like I'll be able to contribute the most playing Mid."
                mc "Sounds great!"
                jump endMaryanneRole

            label maryanneRoleTwo:
                show maryanne smile
                pause(.25)
                ma "I feel like mid would allow me to help everyone and control the pace of the game."
                mc "You can also do that by playing jungle. I can let you jungle if you want."
                show maryanne laugh
                pause(.25)
                ma "What do you think I am? A monkey? You belong in the jungle, not me."
                mc "I can't really argue with that"
                jump endMaryanneRole

            label maryanneRoleThree:
                show maryanne questioning
                pause(.25)
                ma "Huh? But why mid out of all the roles?"
                mc "Well, you seem to enjoy helping other people, and I trust in you to control the pace of the game with your intuition."
                show maryanne blushing
                pause(.25)
                ma "Well... If YOU are suggesting it, I guess I can't refuse."
                mc "Okay then..."
                jump endMaryanneRole
                
            label endMaryanneRole:
                jump endOfRole
        
        label reginaRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Regina"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Regina"
            elif girlsTalkedTo == 3:
                $ whoThird = "Regina"
            show regina glare
            pause(.25)
            mc "Hey Regina."
            r "Hey loser."
            mc "{i}...Why?{/i}"
            mc "Anyways..."
            menu:
                "What role would you enjoy playing?":
                    jump reginaRoleOne
                "Did you understand the game from my explanation?":
                    jump reginaRoleTwo
                "Y-you should consider playing top...":
                    jump reginaRoleThree

            label reginaRoleOne:
                show regina evil smile
                pause(.25)
                r "Oh! Top lane sounds fun since I get to yell at you for help."
                m "Err, you're supposed to be a tank and help teamfight."
                r "So you're telling me I get to smack people around and not die? Even better."
                mc "{i}She's completely missing the point.{/i}"
                show regina glare
                pause(.25)
                r "Hmph, you got a problem with that?"
                mc "U-uh no, not at all."
                show regina smile
                pause(.25)
                r "Good."
                jump endReginaRole

            label reginaRoleTwo:
                show regina rage
                pause(.25)
                r "What? Did you think I'm an idiot or something? Of course I understood what you were talking about. It's not like I'm stupid or anything."
                mc "I wasn't call- Er, nevermind that."
                show regina neutral #nonchalant if avaliable
                pause(.25)
                r "As for my role, I've already decided on Top."
                mc "Huh, why top?"
                show regina evil smile
                pause(.25)
                r "Because I get to tyell at you for help, duh. Oh and I can smack people around."
                mc "That's not the-"
                show regina crossed arms
                pause(.25)
                r "Well, I already made up my mind and you're not chaning it."
                mc "Understood..."
                jump endReginaRole

            label reginaRoleThree:
                show regina stern
                pause(.25)
                r "First of all, don't tell me what to do."
                r "Secondly, shut up."
                r "But purely out of curiosity, why?"
                mc "U-um... you juh-just seem like a t-top..."
                show regina laugh
                pause(.25)
                r "Haha, that is tr -"
                show regina embarrassed
                pause(.25)
                r "I m-mean, shut up!"
                mc "Bu-"
                show regina hand behind back
                pause(.25)
                r "I already told you! You don't know me!"
                r "S-so don't act like you do!"
                mc "I'm sorry..."
                show regina stern
                pause(.25)
                r "Hmph. Fine, I'll pardon you."
                r "Remind me, what does the top do?"
                mc "W-well, the top engages fights and-"
                show regina evil smile
                pause(.25)
                r "Engages fights? That sounds fun."
                r "I'm in! I'll be the top."
                mc "O-okay, it's d-decided. I'm glad that I could he-"
                show regina embarrassed
                pause(.25)
                r "But not because of you!"
                r "Y-you were completely wrong about me!"
                r "So don't go around thinking th-that you helped me or anything!"
                mc "Y-yes, of c-course not..."
                show regina slight smile
                pause(.25)
                r "Hmph. Good."
                mc "{i}I don't know how to feel...{/i}"
                jump endReginaRole                

            label endReginaRole:
                jump endOfRole

        label kristellaRole:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Kristella"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Kristella"
            elif girlsTalkedTo == 3:
                $ whoThird = "Kristella"
            show kristella smile
            pause(.25)
            kr "Hey, [mc]~"
            mc "Hi, Kristella."
            menu:
                "Was there a role that stood out to you?":
                    jump kristellaRoleOne
                "How was my explanation?":
                    jump kristellaRoleTwo
                "Hmm... I think you'd be a great support.":
                    jump kristellaRoleThree
            
            label kristellaRoleOne:
                show kristella smile
                pause(.25)
                kr "Actually, yeah! I'd love to play support."
                mc "Really? Why?"
                kr "Well, I enjoy helping and encouraging people, so I think it fits me perfectly."
                mc "I agree. You're umm... very good at taking c-care of others..."
                show kristella giggle
                pause(.25)
                kr "Hehe ~ that's sweet of you, [mc]."
                mc "Ah... y-you too..."
                mc "{i}What am I even saying? {/i}"
                mc "{i}I should leave now...{/i}"
                jump endKristellaRole

            label kristellaRoleTwo:
                show kristella smile
                pause(.25)
                kr "It was a bit confusing, but I think I got it!"
                mc "That's a relief..."
                mc "Well, do you have a role in mind?"
                kr "Support - it sounds super fun to nourish and care for my teammates!"
                mc "That's great! I think you'll enjoy supporting, too."
                show kristella wink
                pause(.25)
                kr "Oh, I'm sure I will~"
                mc "Um, er - b-bb-, e-excuse me..."
                show kristella giggle
                pause(.25)
                kr "Hehe. Bye, [mc]!"
                jump endKristellaRole

            label kristellaRoleThree:
                show kristella smile
                pause(.25)
                kr "Oh? Why do you say that, [mc]?"
                mc "W-well... I think you're really c-caring and kind, so you'd be good at it..."
                show kristella touched
                pause(.25)
                kr "Aww - thank you, [mc]."
                kr "Also, I was thinking the same~"
                show kristella giggle
                pause(.25)
                kr "I'd love to be your support."
                mc "M-m-mine?!? W-what do you mean?" with hpunch
                kr "Well, you're the captain of the team, silly!"
                kr "That means I'm playing for you."
                mc "..."
                mc "..."
                mc "Oh..."
                kr "Well, see you, [mc]~"
                mc "B-bye -"
                mc "{i}How embarrassing...{/i}"
                jump endKristellaRole

            label endKristellaRole:
                jump endOfRole


        label endOfRole:
            if girlsTalkedTo == 4:
                scene bg clubroom
                mc "Okay, that's everyone! It all worked out, so the roles are decided-"
            else:
                scene bg clubroom
                mc "{i}Who should I talk to next?{/i}"
    $ whoFirst = ""
    $ whoSecond = ""
    $ whoThird  = ""
    $ girlsTalkedTo = 0
    scene bg clubroom
    mc "I'll be the jungler."
    mc "Regina is in the top lane."
    mc "Maryanne is our mid."
    mc "Tiffany is the ADC."
    mc "And last but not least, Kristella is our support!"
    show regina smile
    pause(.25)
    r "That's right."
    hide regina smile
    show tiffany smile
    pause(.25)
    t "Y-yeah."
    hide tiffany smile
    show maryanne smile
    pause(.25)
    ma "Sounds great."
    hide maryanne smile
    show kristella laugh
    pause(.25)
    kr "Woo!"
    hide kristella laugh
    show kelvin smile
    pause(.25)
    kel "Okay, we can start training now."
    mc "Yeah, of course!"
    scene bg clubroom
    mc "{i}Who should I train first?{/i}"
    while girlsTalkedTo <= 3: 
        scene bg clubroom
        menu:
            "Tiffany" if whoFirst != "Tiffany" and whoSecond != "Tiffany" and whoThird != "Tiffany":
                jump tiffanyTraining 

            "Maryanne" if whoFirst != "Maryanne" and whoSecond != "Maryanne" and whoThird != "Maryanne":
                jump maryanneTraining 

            "Regina" if whoFirst != "Regina" and whoSecond != "Regina" and whoThird != "Regina":
                jump reginaTraining 

            "Kristella" if whoFirst != "Kristella" and whoSecond != "Kristella" and whoThird != "Kristella":
                jump kristellaTraining

        label tiffanyTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Tiffany"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Tiffany"
            elif girlsTalkedTo == 3:
                $ whoThird = "Tiffany"
            show tiffany shy
            pause(.25)
            t "I-I guess you're here to teach me?"
            mc "Yeah, we'll go through the basics today."
            show tiffany nervous
            pause(.25)
            t "O-okay, I-I might make a lot of mistakes."
            mc "Don't worry. Everyone makes mistakes whenever they're trying something new."
            t "Y-yeah, I guess..."
            mc "{i}Geez, I wonder how she's going to handle the ingame toxicity.{/i}"
            mc "{i}I hope she doesn't get flamed...{/i}"
            mc "Uh, have you made an account yet?"
            t "U-uh, yea. M-my username is KawaiiTiff."
            mc "Oh..."
            menu:
                "I like your name":
                    jump tiffanyNameOne
                "What did you base your name on?":
                    jump tiffanyNameTwo
                "Interesting name...":
                    jump tiffanyNameThree

            label tiffanyNameOne:
                show tiffany shy
                pause(.25)
                t "U-uh, t-thanks."
                mc "What does kawaii mean?"
                show tiffany flustered
                pause(.25)
                t "U-uagh, i-it m-means c-c-cute in Japanese."
                mc "Oh, it suits you well."
                show tiffany blush 
                pause(.25)
                t "C-can we get on with the lesson?"
                jump tiffanyNameEnd
            
            label tiffanyNameTwo:
                show tiffany flustered
                pause(.25)
                t "U-uah, K-Kawaii m-means c-c-cute in Japanese."
                mc "Oh, I see, it fits your personality well."
                t "T-thanks. C-can we s-start the lesson now?"
                jump tiffanyNameEnd
            
            label tiffanyNameThree:
                show tiffany shy
                pause(.25)
                t "T-t-thanks..."
                mc "{i}I didn't know she was a weeb...{/i}"
                t "U-uh why are you staring at me."
                mc "Oh, I was just thinking."
                t "O-oh, c-can we s-start the lesson?"
                jump tiffanyNameEnd

            label tiffanyNameEnd:
                scene bg computer

            mc "Alright, we should..."
            menu:
                "Go into a pvp match.":
                    jump tiffanyTrainingOne
                "Play some 1v1s.":
                    jump tiffanyTrainingTwo
                "Have you watch me for a bit.":
                    jump tiffanyTrainingThree

            label tiffanyTrainingOne:
                show tiffany shocked
                pause(.25)
                t "W-wait, a PvP match??? S-shouldn't I practice against bots or something to learn the game?"
                mc "Well, most players do, but since we're playing in a tournament soon, we need to improve quickly and I think by going straight into PvP is the best way to do that."
                show tiffany neutral
                pause(.25)
                t "O-okay. So I just click on this?"
                mc "Yes. Then just accept the game when it pops up."
                show tiffany shocked
                pause(.25)
                t "Oh. I-I got a game."
                mc "Ok so just type that you're playing ADC."
                show tiffany neutral
                pause(.25)
                t "Okay so what champ should I play."
                mc "I think Bane would be a good champion for you."
                scene bg computer game
                with fade
                mc "Alright so you should..."
                menu:
                    "Focus on last hitting the creeps.":
                        jump TiffanyPVPOne
                    "Try to kill the enemy.":
                        jump TiffanyPVPTwo
                
                label TiffanyPVPOne:
                    show tiffany neutral 
                    pause(.25)
                    t "S-so do I just hit them like this."
                    mc "No, no, no, wait until it's low then hit it."
                    t "O-oh so like thi-. I-I didn't get it."
                    mc "Don't worry, it takes time to get used to- oh they're trying to kill you."
                    show tiffany scared
                    pause(.25)
                    t "W-what d-do I do, they're hitting me. [mc] h-help!"
                    mc "Well, you fight bac- oh you died."
                    mc "{i}This is going to be harder than I thought{/i}"
                    jump tiffanyPVPEnd

                label TiffanyPVPTwo:
                    mc "Alright so when you level up start attacking the enemy."
                    show tiffany confused
                    pause(.25)
                    t "D-do I just walk up and-?"
                    mc "NO DON'T WALK-. Well you're dead."
                    t "O-oh, I-I died so fast..."
                    mc "yeah, you have to be careful with their abilities."
                    mc "{i}This is going to be a long day...{/i}"
                    jump tiffanyPVPEnd

                label tiffanyPVPEnd:
                    scene bg computer
                    with fade
                
                show tiffany exhausted
                pause(.25)
                t "W-wow I won, even though I died a lot."
                mc "{i}For a new player, she isn't that bad.{/i}"
                mc "Nice job. I'll point out your mis-."
                scene bg computer
                mc "{i}Wait, why is she typing so much?{/i}"
                mc "{i}???{/i}"
                mc "{i}Whoa whoa, this is the kind of stuff that you have to censor really heavily, just a bit of pixelation won't cut it..."
                show tiffany shy
                pause(.25)
                mc "..."
                t "[mc]? I-is something wrong? You've been staring at me for a bit..."
                mc "..."
                mc "{i}Isn't she usually super quiet?{/i}"
                t "[mc]???"
                mc "..."
                mc "{i}Why is she toxic in game?{/i}"
                t "G-guys? [mc] looks really pale... He stopped breathing! Guys h-help!"
                mc "I-I'm fine. M-maybe we can review your game next time..."
                t "A-are y-you sure?"
                mc "{i}I should disable her chat function{/i}"
                mc "Y-yea, see you."
                t "B-bye."
                jump tiffanyTrainingEnd

            label tiffanyTrainingTwo:
                show tiffany shocked
                pause(.25)
                t "W-wait, a 1v1? W-with you? Aren't you really good at this game?"
                mc "Exactly. I'm Diamond, so I'm farm better than the average player. By playing against better competition, you'll learn quicker."
                t "I guess you're right. S-so what champ should I play?"
                mc "I think Bane is a good champion for you."
                scene bg computer game
                with fade
                mc "{i}Hmm, it's been 5 minutes and she is getting low on health.{/i}"
                mc "{i}I am getting a little bored{/i}"
                mc "{i}Should I...{/i}"
                menu:
                    "Try to kill her.":
                        jump tiffany1v1One
                    "Play patiently.":
                        jump tiffany1v1Two
                    "Let her kill me.":
                        jump tiffany1v1Three

                label tiffany1v1One:
                    mc "{i}Ok, so I will just start my combo off and...{/i}"
                    mc "!!!" with hpunch
                    show tiffany confused
                    pause(.25)
                    t "U-uh, h-how did you miss everything?"
                    mc "{i}How did she dodge everything? Maybe I'll just...{/i}"
                    "You have been slain." #maybe play audio file of league announcer instead
                    t "O-oh, I-I killed you. Y-you went easy on my right?"
                    mc "H-how di...err yeah, I didn't try that hard, good job surviving the assault."
                    mc "{i}I can't believe I died to the turret.{/i}"
                    mc "Anyways, are you ready for round 2?"
                    show tiffany confident
                    pause(.25)
                    t "Bring it on!"
                    jump tiffany1v1End
            
                label tiffany1v1Two:
                    mc "{i}I'll just wait until she makes a mistake and k-"
                    mc "!!!"
                    show tiffany annoyed 
                    pause(.25)
                    t "W-why are you playing so far back?"
                    mc "{i}Wow that was close. Now I can...{/i}"
                    t "S-stop running away from me.L-let me-"
                    "An enemy has been slain."
                    t "O-oh... I died."
                    mc "{i}Phew that was close.{/i}"
                    mc "That was a good try. Next time, make sure to dodge my attacks."
                    t "U-understood."
                    jump tiffany1v1End

                label tiffany1v1Three:
                    mc "{i}Okay, so I just let her attack me and I'll run under her turret. This should be good for her confidence.{/i}"
                    show tiffany confused
                    pause(.25)
                    t "[mc]? W-what are you doing?"
                    mc "Hmm? Doing what?"
                    "You have been slain."
                    mc "Ah, I guess you killed me. Good job."
                    t "Y-you didn’t try very hard did you?"
                    mc "O-of course I was trying..."
                    t "Y-you were just bored of playing right?"
                    mc "Y-yea, I guess. I'm sorry."
                    t "N-next time can you g-go a little harder? I-I promise I w-won’t be boring."
                    mc "Alright."
                    jump tiffany1v1End

                label tiffany1v1End:
                    scene bg computer
                    with fade
                
                mc "{i}She has good mechanics. Just need to work on-{/i}"
                mc "{i}Why is she typing to me?{/i}"
                mc "!!!" with hpunch
                show tiffany smile 
                pause(.25)
                t "W-wow I got completely destroyed. I gu- [mc]?"
                mc "{i}Whoa whoa, this is the kind of stuff that you have to censor really heavily, just a bit of pixelation won't cut it..."
                t "[mc]?!?"
                mc "..."
                mc "{i}I'm surprised she has so much to say when she's usually so quiet.{/i}"
                show tiffany shocked
                pause(.25)
                t "G-guys? I-I think [mc] needs h-help!"
                mc "N-no need. I’m fine. I’ll tell you what you did wrong at the next meeting."
                t "A-are you sure?"
                mc "{i}I should disable her ability to chat in game. I didn’t expect her to be so toxic.{/i}"
                mc "Y-yea, bye."
                jump tiffanyTrainingEnd

            label tiffanyTrainingThree:
                show tiffany confused
                pause(.25)
                t "U-uh shouldn't I play against bots to practice?"
                mc "Well, it helps to watch someone who knows what they are doing."
                show tiffany understanding
                pause(.25)
                t "O-oh I see..."
                mc "Anyways, I'll just queue up as ADC and play Bane."
                show tiffany confused
                pause(.25)
                t "W-who's Bane?"
                mc "He's a playable character that I think fits you."
                scene bg computer game
                with fade
                mc "{i}It's so boring right now. The enemy is low but the support doesn't want to fight. I've already explained the basics to Tiffany.{/i}"
                mc "{i}Should I-{/i}"
                menu:
                    "Start attacking the enemy.":
                        jump tiffanyWatchOne
                    "Wait for the enemy to make a mistake.":
                        jump tiffanyWatchTwo
                    "Tell the support to fight.":
                        jump tiffanyWatchThree

                label tiffanyWatchOne:
                    mc "Alright, Tiffany never imitate what I am about to do because it's reckless."
                    show tiffany confused 
                    pause(.25)
                    t "H-huh, i-isn't the enemy almost dead? W-why don-"
                    hide tiffany confused
                    "You have been slain."
                    mc "Ah, I misplayed that fight. This is why you shou-"    
                    "An enemy has been slain."
                    mc "Ah, he died to creeps. Anyways, never go for that kill because if you die and the enemy doesn't, the game becomes very unplayable."
                    show tiffany understanding
                    pause(.25)
                    t "O-oh, I-I understand now. I-if you have the a-advantage, you shouldn't gamble it away."
                    mc "I guess you could put it that way."
                    mc "{i}Wow, she's a fast learner.{/i}"
                    jump tiffanyWatchEnd

                label tiffanyWatchTwo:
                    mc "Ok Tiffany, now that the enemy is low, I'll wait for him to make a mistake. Then I can kill him."
                    show tiffany confused
                    pause(.25)
                    t "B-but how can y-you tell when he makes a mistake?"
                    mc "Well, you need to- oh he's so dead."
                    hide tiffany confused
                    "An enemy has been slain."
                    mc "Oh? The support is also running in?"
                    "Double Kill."
                    mc "Well, that was two easy kills. As I was saying, you need to be able to tell when he’s in kill range and how far your abilities travel. When he gets a little too close, you can kill him, but make sure you don’t miss."
                    show tiffany understanding
                    pause(.25)
                    t "O-oh, s-so when he gets too close and is low on health, s-start attacking?"
                    mc "Uh, sounds about right."
                    mc "{i}She's grasping the basics pretty fast.{/i}"
                    jump tiffanyWatchEnd

                label tiffanyWatchThree:
                    mc "Ok, so now that the enemy is low, I am going to tell my support to start attacking and I will follow."
                    show tiffany confused
                    pause(.25)
                    t "H-huh? W-why the support? W-why not just go in by yourself?"
                    mc "Well... If I go in by myself, it - oh he missed. Whatever, the enemy is still dead."
                    hide tiffany confused
                    "An enemy has been slain."
                    mc "As I was saying, you should tell the support to start attacking because if you attack by yourself, it becomes a 1v2 and it’s very likely you die. Also, the support typically has abilities that restrain the enemy’s movement."
                    t "U-uh, s-so the support goes in to restrain the enemy so it's easier to kill? I-I'm kind of confused."
                    mc "That's right!"
                    mc "I thought it would be harder to teach her, but she's learning pretty quickly."
                    jump tiffanyWatchEnd

                label tiffanyWatchEnd:
                    scene bg computer
                    with fade
                    mc "Nice, I won. That game was pretty easy since I got a lot of kills."
                    t "C-can I see the keyboard and mouse for a bit?"
                    mc "Oh? You want to see my settings? It's understandable since I'm so g-"
                    pause
                    mc "{i}Wait a minute...{/i}"
                    mc "{i}W-wha? It shounds like she's typing an essay. What is she-{/i}"
                    mc "!!!" with hpunch
                    mc "{i}Woah, woah, woah. This is the type of stuff that you have to censor heavily, just a bit of pixelating won't cut it.{/i}"
                    show tiffany shy
                    pause(.25)
                    t "A-alright you can hav- MC???"
                    mc "..."
                    mc "{i}Wait, I might get chat restricted.{/i}"
                    t "[mc]???"
                    mc "..."
                    mc "{i}Please don't get chat restricted. I still need to get my rewards.{/i}"
                    t "G-guys, help. I-I think [mc] is-"
                    mc "I-I’m fine. Don’t worry about me. I-I think our training session is done."
                    t "B-but I didn't play yet."
                    mc "I'll watch you play next time."
                    t "O-oh, okay. B-bye."
                    mc "See ya."
                    mc "{i}I need to disable her chat or else she might get banned.{/i}"
                    jump tiffanyTrainingEnd

            label tiffanyTrainingEnd:
                jump endOfTraining

        label maryanneTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Maryanne"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Maryanne"
            elif girlsTalkedTo == 3:
                $ whoThird = "Maryanne"
            show maryanne excited
            pause(.25)
            ma "Hey [mc]! I'm ready to learn the basics of the game!"
            mc "{i}She has a lot of energy.{/i}"
            mc "Alright, I'm assumiing you have an account already?"
            ma "Yep! My account is called Stan Jae."
            mc "{i}She's a koreaboo?{/i}"
            ma "[mc]? What's wrong?"
            menu:
                "Uh, interesting name.":
                    jump maryanneNameOne
                "is that a kpop singer?":
                    jump maryanneNameTwo
                "I like your name!":
                    jump maryanneNameThree
            
            label maryanneNameOne:
                show maryanne excited
                pause(.25)
                ma "O-oh, I'm not very creative with names."
                mc "He's a member of Day6 right?"
                show maryanne blush
                pause(.25)
                ma "Yea! He's so cute and reminds me of someone."
                mc "{i}Why does it feel so hot in this room?{/i}"
                mc "Hmm, I wonder who...?"
                ma "Isn't it pretty obvious?"
                mc "Uhh, not really... Anyways, we're getting off topic."
                show maryanne neutral
                pause(.25)
                ma "Oh right! What do you want me to do again?"
                jump maryanneNameEnd

            label maryanneNameTwo:
                show maryanne excited
                pause(.25)
                ma "Yeah! He's a member of Day6 and he's super cute."
                mc " I didn't know you were into kpop."
                ma "Oh I love kpop! We should listen to it while you coach me!"
                mc "U-uh, I'm good."
                show maryanne pout
                pause(.25)
                ma "You probably listen to EDM or something."
                mc "{i}EDM is good though...{/i}"
                mc "W-we're getting off topic."
                show maryanne neutral
                pause(.25)
                ma "Oh right! What do you want me to do again?"
                jump maryanneNameEnd

            label maryanneNameThree:
                show maryanne excited
                pause(.25)
                ma "Oh really?! You also listen to kpop?!?"
                mc "Well, I occasionally do. Jae's a member of Day6 right?"
                show maryanne blush
                pause(.25)
                ma "Yea! He's so dreamy, like a certain someone."
                mc "{i}I guess kpop idols are pretty hot...{/i}"
                mc "I guess yo- Huh, what are you staring at?"
                show maryanne flustered
                pause(.25)
                ma "O-oh n-nothing!"
                mc "Ah, forget it. We're getting off topic."
                show maryanne neutral
                pause(.25)
                ma "Oh yea! So what should I do?"
                jump maryanneNameEnd

            label maryanneNameEnd:
                scene bg computer
                mc "Well, you should..."
            menu:
                "Play a PvP Game":
                    jump maryanneTrainingOne
                "1v1 me.":
                    jump maryanneTrainingTwo
                "Watch me play a game.":
                    jump maryanneTrainingThree

            label maryanneTrainingOne:
                show maryanne confused
                pause(.25)
                ma "A PvP game? Don’t I need to learn the game first?"
                mc "Well yes, but you’ll learn faster by playing against other people. Besides, I’ll be helping you so don’t worry."
                show maraynne neutral
                pause(.25)
                ma "If you say so... So do I just press this option?"
                mc "Yep! Then we just wait for a game."
                pause(3)
                ma "Oh! I got a game!"
                mc "Okay so now, type mid to let the other players know where you are going."
                ma "Done! So who should I play? Fang? Synk? Pyre?"
                mc "You like to help impact the map right? Hmm, I think Straight Fate would be a good character to play."
                ma "Hmmm, alright if you say so."
                mc "{i}Now to teach her the basics...{/i}"
                scene bg computer game
                with fade
                mc "{i}Seems like the game is going well right now. She hasn’t died, but is around half health, same with her opponent. It seems they are about to level up and get their ultimate moves. I should tell her to…{/i}"
                menu:
                    "Back off and be careful.":
                        jump maryannePvPOne
                    "Go help another lane.":
                        jump maryannePvPTwo
                    "Help her jungler.":
                        jump maryannePvPThree

                label maryannePvPOne:
                    mc "Hey Maryanne, you should back off and play safer."
                    show maryanne confused
                    pause(.25)
                    ma "Huh? Why do I need to back off? I think I'm doi-"
                    mc "WATCH OUT! The enemy just got his ultimate... I'm pretty sure you're dead."
                    hide maryanne confused
                    "You have been slain."
                    show maryanne neutral
                    pause(.25)
                    ma "Oh, well. I guess I died haha. But why should I back off? Wouldn’t I get my ultimate the same time as him?"
                    mc "Uh, well, his ultimate allows him to do more damage while your ultimate is more of a utility that allows you to impact the map."
                    show maryanne understanding
                    pause(.25)
                    ma "Oooohh, so since my ultimate isn’t good for 1v1 and my opponent’s is, I should be careful when he has it?"
                    mc "That's the gist of it."
                    mc "{i}Wow I'm surprised she got all that from just a simple explanation.{/i}"
                    jump maryannePvPEnd

                label maryannePvPTwo:
                    mc "Maryanne, you should go help another lane."
                    show maryanne confused
                    pause(.25)
                    ma "Do I just start walking to the top lane?"
                    mc "No, no, you just got your ultimate, just use it to instantly travel there and kill the enemy."
                    show maryanne understanding
                    pause(.25)
                    ma "Ohhhh, so like this?"
                    mc "NOT UNDER T-"
                    hide maryanne understanding
                    "You have been slain."
                    "An enemy has been slain."
                    mc "I guess you helped kill the enemy so it’s not the worst that can happen. Just make sure not to teleport into a dangerous spot."
                    show maryanne understanding
                    pause(.25)
                    ma "So basically, my ultimate allows me to make a 1v1 into a 2v1 in favor of my teammate, but if I teleport too far away, I put myself at risk of dying?"
                    mc "Sounds about right."
                    mc "{i}That's what I was going to say next...{/i}"
                    jump maryannePvPEnd
                
                label maryannePvPThree:
                    mc "Hey, your jungler is fighting the enemy jungler, you should go help him. You should use your ultimate to teleport there."
                    show maryanne confused 
                    pause(.25)
                    ma "Do I just click here to teleport?"
                    mc "Yep! Now just kill the enemy jungler."
                    hide maryanne confused
                    "An enemy has been slain."
                    mc "Nice! You should always help your jungler if he’s in trouble. It will allow him to push the tempo and make aggressive plays."
                    show maryanne understanding
                    pause(.25)
                    ma "Ohh, so I should go help my jungler win the 1v1, then go impact somewhere on the map since the enemy won’t know where we’re going to go and their jungler can’t answer it?"
                    mc "Basically yeah."
                    mc "{i}I'm surprised she actually understood all of that.{/i}"
                    jump maryannePvPEnd

                label maryannePvPEnd:
                    scene bg computer 
                    with fade
                show maryanne happy
                pause(.25)
                ma "I can't believe we just won."
                mc "Nice job on winning your first game."
                ma "Well, it was all thanks to you. Nii-chan is such a good coach."
                mc "I can’t just take all the credit. You pulled in yo-Wait, did you just call me-"
                show maryanne flustered
                pause(.25)
                ma "N-NO! I DIDN’T SAY ANYTHING. YOU MUST HAVE HEARD SOMETHING WRONG."
                mc "{i}Why is she so flustered?{/i}"
                mc "I-I guess so… Anyways, we’re running out of time. I’ll review your game at the next meeting."
                ma "O-okay, B-bye [mc]."
                mc "S-see ya."
                mc "{i}I wonder why she was in a hurry to get out of there…{/i}"
                jump maryanneTrainingEnd

            label maryanneTrainingTwo:
                show maryanne shocked
                pause(.25)
                ma "1v1 YOU? Aren’t you way out of my league??"
                mc "Well, I am pretty hot."
                show maryanne blushing
                pause(.25)
                ma "I MEAN IN LL YOU DUMMY!!!"
                mc "Oh. I mean, even if I am way better than you, it’ll help you improve and learn the game much quicker."
                show maryanne pout
                pause(.25)
                ma "Sounds like an excuse to just beat me over and over."
                mc "{i}She's not wrong...{/i}"
                mc "Don't worry, I'll take it easy on you."
                ma "You promise?"
                mc "Yes… Ok so I think you should play Straight Fate. Even though he is better to learn in a PvP game, it should be okay to use him to learn the basics."
                ma "It sounds like you're just making it easier to kill me."
                mc "No, no, no, it's for pract-"
                show maryanne giggle #use smile if image not present
                pause(.25)
                ma "Hehe, I know, I was just messing with you."
                mc "..."
                scene bg computer game
                with fade
                mc "{i}I can’t believe she survived for this long. Well, I guess it makes sense since she was playing so safe. Hmm, maybe I should just…{/i}"
                menu:
                    "Go kill her":
                        jump maryanne1v1One
                    "Wait for a bit, then kill her.":
                        jump maryanne1v1Two
                    "Let her kill me.":
                        jump maryanne1v1Three
                
                label maryanne1v1One:
                    


            label maryanneTrainingEnd:
                jump endOfTraining
                

        label reginaTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Regina"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Regina"
            elif girlsTalkedTo == 3:
                $ whoThird = "Regina"

        label kristellaTraining:
            $ girlsTalkedTo += 1
            if girlsTalkedTo == 1:
                $ whoFirst = "Kristella"
            elif girlsTalkedTo == 2:
                $ whoSecond = "Kristella"
            elif girlsTalkedTo == 3:
                $ whoThird = "Kristella"

        label endOfTraining:
            if girlsTalkedTo == 4:
                mc "Oh wait, we should head back."
                scene bg clubroom                
            else:
                scene bg clubroom
                mc "{i}Who should I talk to next?{/i}"


    return
